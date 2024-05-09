from bs4 import BeautifulSoup

with open('../data/answers.csv', 'r', encoding='utf-8') as rf, open('../data/answers_clear.csv', 'w', encoding='utf-8') as wf:
    head = rf.readline()
    wf.write(head)
    length = len(head.strip().split(','))
    lines = rf.readlines()

    for line in lines:
        ls = line.strip().split(',')
        if len(ls) == length:
            # 假设我们要清洗的是列表中的最后一个元素，即内容字段
            content = BeautifulSoup(ls[-1], "lxml").get_text()  # 使用BeautifulSoup去除HTML标签
            ls[-1] = content  # 将去除了HTML标签的内容替换回原列表
            wf.write(','.join(ls) + '\n')  # 注意在写回文件时添加换行符'\n'