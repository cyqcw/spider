import requests
import json
import time
from entity import *


# 目标URL
url = "https://www.zhihu.com/api/v4/search_v3"
nextUrl = None
# 关键词
keyWords = ['人工智能']
# 每页大小
pageSize = 20
questionPath='./data/questions.txt'
articlePath='./data/articles.txt'

# 请求头
headers = {
    # "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    # 以下Cookie和其他特定头信息可能需要根据实际情况调整
    "Cookie": "_zap=0e195c0c-98b9-4a14-aa13-6121ae2c74cd; d_c0=ALBU2ZcilhePTrLjK5IA1cOhFMf6zwRoPlc=|1697992389; __snaker__id=olApQtmhiwbmpeyX; _xsrf=NDWkyb0gZvkQFH8ABcYYX87T5wMz0G4o; q_c1=4cdd7e30e6a34f3ba66b2834adbe5613|1713582633000|1713582633000; z_c0=2|1:0|10:1713582742|4:z_c0|92:Mi4xMlJxOUZBQUFBQUFBc0ZUWmx5S1dGeGNBQUFCZ0FsVk5LSUFRWndDVnFhZldWMi1zVThRYk14YjVIYVNuOVhaXzZ3|950cf96b0e1e4ea6e0e77724c71210d40e7ec4f45bff922e578a29f29a7a7633; gdxidpyhxdE=4%2FL%5C4dOnkuuVizqagsXEWBvWH%2FVk4GIO7S9fXJlaCMWb3r%5ColdAmp%5CSNE2x3K9vnKUqt8JUvD9Kel7c0naOlePc66KHJzRSOy5hMVavRmZJ38MjQUt8%5CKYmclUulJbZz03CbOo%2FGOXtqE8hXgN%2Fc6%5CysHLWvUPmvN12%2BHo3o6TVSGYwc%3A1714208638670; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1714015142,1714037265,1714186028,1714381984; tst=r; SESSIONID=NJQdqK0BUk68p3oa3DJce9JTTRWawxSg4k39gMIIxoo; JOID=VF4XBk3HPjR3FFuub8RuYnFXgDR8iXBiEGUQmiqSVQZIZ2jBCqCqABIUX61rudGnl_a6HFXdB8pg0Yw2dRqEdtw=; osd=VVwWA0LGPDVyG1qsbsFhY3NWhTt9i3FnH2QSmy-dVARJYmfACKGvDxMWXqhkuNOmkvm7HlTYCMti0Ik5dBiFc9M=; BEC=43d4532fd57f0c3c659e43172114057d; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1714466211; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1714466211|1714460510",
    "X-Api-Version": "3.0.91",
    # "X-App-Za": "OS=Web",
    # "X-Requested-With": "fetch",
    "X-Zse-93": "101_3_3.0",
    # 需要根据实际情况调整
    "X-Zse-96": "2.0_5KcY6+pyb96B4BbWLB1GG5Qtp6DUvzQZS6+crUkSGRn=ZzASW9WHNK5t8D1In0cG"
}

XZse96Array=[
    '2.0_QzfPpdX4UgRyBl/10Tk0YdfwaeLdvHvODvwur0eyNzz3fBzSUMxhjkbAS=mlUXxn',
    '2.0_ivWkDn0UwlrM5ULuPJHfnVMv4nScXqUTm04kYy98v=cMzBNPixZc=tCVX=AKfwoW',
    "2.0_7+5or63nFlL5NixDmy8sDRyYMpmV0Su4t7aNhkmdXj6kxvrDUZU6o+GavUfWD4Z5",
    '2.0_V6ya3xcdKHO=zCU4yFi=jucegwaq+Qsrh7/F/Yzf1za=zcm0VKktcO8hOCrCpae0',
    '2.0_k0XQAThGxeGyyfgfwnoOBLzkmTbOB5FBlHuGy0TeI1=jHbp+7liik0+y=1a1H=Rj',
    '2.0_SohACevrc8xprQ9pkHD+8i9CPacrUU/IiceJbTa6aCI/HD3p4NYsBBnvZGs5juiZ',
]

# 查询参数
params = {
    "gk_version": "gz-gaokao",
    "t": "general",
    "q": "人工智能",
    "correction": "1",
    "offset": "0",
    "limit": str(pageSize),
    "filter_fields": "",
    "lc_idx": "0",
    "show_all_topics": "0",
    "search_source": "Normal",
}

# 问题URL列表
questions = []
questionUrls = []

articles= []
articleUrls = []

# 根据关键词检索获得问题URL
def getQuestionUrls(keyWord:str)->None:
    page=0
    # 每次循环获取一页数据(20个问题/文章)，直到没有数据
    while True:
        # 发送GET请求
        response = requests.get(url, params = params, headers=headers)
        
        # 检查响应状态码
        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}, reason: {response.reason}, text: {response.text}")
            break
        
        # 解析JSON内容
        content = json.loads(response.content.decode('utf-8'))
        
        # 如果后续没有数据，退出循环
        if content['paging']['is_end']:
            break
        
        # 解析获取这一页的问题URL
        for data in content['data']:
            if data['type'] != 'search_result':
                continue
            object= data['object']
            # 如果是问题
            if object['type'] == 'answer': 
                question = object['question']
                print(f"page: {page}, index: {data['index']}, dataHeight: {question['name']}")
                # 如果问题URL不在列表中，添加到列表
                if question['url'] not in questionUrls:
                    questions.append(Question(
                        question['id'], question['type'], question['name'],
                        question['url'], question['answer_count'], question['follow_count']    
                    ))
                    questionUrls.append(question['url'])
            # 如果是文章
            elif object['type'] == 'article':
                article = object
                print(f"page: {page}, index: {data['index']}, dataHeight: {article['title']}")
                # 如果文章URL不在列表中，添加到列表
                if article['url'] not in articleUrls:
                    articles.append(Article(
                        article['id'], article['author']['id'], article['author']['name'],
                        article['author']['url'], article['author']['type'], article['author']['headline'],
                        article['title'], article['type'], article['url'], article['excerpt'],
                        article['voteup_count'], article['comment_count'], article['zfav_count'],
                        article['created_time'], article['updated_time'], article['content']
                    ))
                    articleUrls.append(article['url'])
            else:
                print(f"未知类型：{object['type']}, {data['index']}")
                
        # 下一页
        nextUrl = content['paging']['next']
        print(f"nextUrl: {nextUrl}")
        page+=1
        if page>10:
            break
        
        params['offset'] = str(page * pageSize)
        params['search_hash_id'] = content['search_action_info']['search_hash_id']
        params['lc_idx'] = str(page * pageSize)
        params['vertical_info'] = '0,1,0,0,0,0,0,0,0,0'
        params['search_source'] = 'Normal'
        print(f"params: {params}")
        time.sleep(1)


def saveQuestionsToPath(path:str)->None:
    with open(path, 'w+', encoding='utf-8') as f:
        for question in questions:
            f.write(f"{question}\n")
    print(f"问题数量：{len(questions)}")
    
def saveArticlesToPath(path:str)->None:
    with open(path, 'w+', encoding='utf-8') as f:
        for article in articles:
            f.write(f"{article}\n")
    print(f"文章数量：{len(articles)}")


if __name__ == '__main__':
    getQuestionUrls('人工智能')
    saveArticlesToPath(articlePath)
    saveQuestionsToPath(questionPath)
    



