import requests
import json
import time
from entity import *


# 目标URL
url = "https://www.zhihu.com/api/v4/search_v3"
nextUrl = None 
"""
"next": "https://api.zhihu.com/search_v3?
advert_count=0\u0026
correction=1\u0026
filter_fields=\u0026
gk_version=gz-gaokao
\u0026lc_idx=0\u0026
limit=20\u0026
offset=20\u0026
q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD\u0026
search_hash_id=c9a5ff6c8ecaf556f96ac8a441fddd5d\u0026
search_source=History\u0026
show_all_topics=0\u0026
t=general\u0026
vertical_info=0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0"
"""
# 关键词
keyWords = ['人工智能']
# 每页大小
pageSize = 20
questionPath='questions.txt'
articlePath='articles.txt'

# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    # 以下Cookie和其他特定头信息可能需要根据实际情况调整
    "Cookie": "_zap=0e195c0c-98b9-4a14-aa13-6121ae2c74cd; d_c0=ALBU2ZcilhePTrLjK5IA1cOhFMf6zwRoPlc=|1697992389; __snaker__id=olApQtmhiwbmpeyX; _xsrf=NDWkyb0gZvkQFH8ABcYYX87T5wMz0G4o; q_c1=4cdd7e30e6a34f3ba66b2834adbe5613|1713582633000|1713582633000; z_c0=2|1:0|10:1713582742|4:z_c0|92:Mi4xMlJxOUZBQUFBQUFBc0ZUWmx5S1dGeGNBQUFCZ0FsVk5LSUFRWndDVnFhZldWMi1zVThRYk14YjVIYVNuOVhaXzZ3|950cf96b0e1e4ea6e0e77724c71210d40e7ec4f45bff922e578a29f29a7a7633; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1714013395,1714015142,1714037265,1714186028; gdxidpyhxdE=4%2FL%5C4dOnkuuVizqagsXEWBvWH%2FVk4GIO7S9fXJlaCMWb3r%5ColdAmp%5CSNE2x3K9vnKUqt8JUvD9Kel7c0naOlePc66KHJzRSOy5hMVavRmZJ38MjQUt8%5CKYmclUulJbZz03CbOo%2FGOXtqE8hXgN%2Fc6%5CysHLWvUPmvN12%2BHo3o6TVSGYwc%3A1714208638670; BEC=f3a75d7265fd269b7c515e5c94175904; tst=r; SESSIONID=B6CDY1zqrxah1TF7DN6tB3UGhSWi3araHE0P5aJXd5s; JOID=UlsdAUkG6egJDiJQSAS4sg1D-MtXR9ShTVUQITN2koJrP3QVdAcpzm0PKlFCF3QMiuAHzUDgI6gJnifDQGMRuUU=; osd=W1oQC0wP6OUDCytRRQ69uwxO8s5eRtmrSFwRLDlzm4NmNXEcdQojy2QOJ1tHHnUBgOUOzE3qJqEIky3GSWIcs0A=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1714209066; KLBRSID=ca494ee5d16b14b649673c122ff27291|1714209066|1714202070",
    "X-Api-Version": "3.0.91",
    "X-App-Za": "OS=Web",
    "X-Requested-With": "fetch",
    "X-Zse-93": "101_3_3.0",
    # 需要根据实际情况调整
    "X-Zse-96": "2.0_t8AqDH=tPzk2NKV3L5WdhSktS12DwDqcwB2Xqam7Dnh5SSrASZJUZlRI=2r5J7f1"
}

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
    "search_source": "History",
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
        response = requests.get(url, params= params, headers=headers)
        
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
    



