# 阿里云大模型示例
import csv
import random
import time
from http import HTTPStatus
import dashscope
from dashscope import Generation

questionPath = "../zhihu/data/questions.csv"
def getAlreadyQuestions() -> list:
    alreadyQuestions = []
    try:
        with open(questionPath, 'r', encoding='utf-8') as qu:
            readerQu = csv.DictReader(qu)
            for row in readerQu:
                alreadyQuestions.append(row['name'])
    except FileNotFoundError:
        print(f"警告：文件 {questionPath} 未找到。")
    return alreadyQuestions

def call_stream_with_messages(question):
    dashscope.api_key = 'sk-Re29MpP6Lg'
    messages = [
        {'role': 'user', 'content': question}
    ]
    responses = Generation.call(
        'qwen1.5-110b-chat',
        messages=messages,
        seed=random.randint(1,1000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message"  format.
        stream=True,
        output_in_full=False  # get streaming output incrementally
    )
    full_content = ''
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            full_content += response.output.choices[0]['message']['content']
            # print(response)
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    print('Full content: \n' + full_content)
    return full_content

if __name__ == '__main__':
    alreadyQuestions = getAlreadyQuestions()
    # 打开或创建一个 CSV 文件，并准备写入数据
    with open("data/answer_new.csv", 'a+', newline='', encoding='utf-8') as csvfile:
        # 定义 CSV 文件的列名
        fieldnames = ['question', 'answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头（如果文件是新建的，则需要写入表头；如果是追加模式下打开的已有文件，表头只需写入一次）
        csvfile.seek(0)
        if csvfile.read(1) == '':
            writer.writeheader()

        # 遍历问题列表，获取每个问题的答案，并写入 CSV 文件
        for question in alreadyQuestions:
            answer = call_stream_with_messages(question)
            writer.writerow({'question': question, 'answer': answer})
            # 随机等待 2 到 5 秒
            time.sleep(random.randint(2, 5))
