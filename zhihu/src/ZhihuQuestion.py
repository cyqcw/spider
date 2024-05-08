import csv
import random

import execjs
import requests
import json
import time
from entity import *
from urllib.parse import urlencode

# 目标接口
baseUrl = "https://www.zhihu.com/api/v4/search_v3"

# 关键词
keyWords = ['人工智能']

# 保存路径
questionPath = '../data/questions.csv'
articlePath = '../data/articles.csv'

# 请求头
headers = {
    "authority": "www.zhihu.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "_zap=55d70801-1690-43db-b4d0-cf16a2aa28ec; d_c0=AHAXJUx5xRaPTo1CHUTt-lh3rGIt69EcLO0=|1683989365; _xsrf=bdcf3a25-1208-4b12-a969-212abb21f4c0; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1714544962,1715162121; SESSIONID=Tlz9iMcdUF5G9QXw4YySWbxgdZvxVJOSESgOUfFYvFM; JOID=W14VBkyCL2d9wAOkK44-Nt98VuY62UUYRqdBwUrZZlQ_-1zzWoFgWxfBCqcs19fppIZ6sb5yQ--S-deFCQftWSo=; osd=UVEUAkyIIGZ5wAmrKoo-PNB9UuYw1kQcRq1OwE7ZbFs-_1z5VYBkWx3OC6Ms3djooIZwvr92Q-Wd-NOFAwjsXSo=; __snaker__id=814B6gFAkw6uGCWd; captcha_session_v2=2|1:0|10:1715162158|18:captcha_session_v2|88:RVd2U2p6OXV0azVpYmJua0d4RTBQcENRWFNVdUF6S1MzSVBYeHdBMzZVSnZ1aDNBWFZNdkU0T1BDSXVkRmpMNA==|2521e3ba553976d936ff223ec6d2d31c61fb63f45dd635f813411848144f92f4; gdxidpyhxdE=2d3HTwbGoEeqebE1HKg9D8nTEGOXRz4pBE3UQ63wMen2ifBgevSenMhsJi0PSNA5n%2B1RQM%5CnJioz%5CbAsaat3bC6D2RZQQ0YsT913yVsbxMgbWJ1aUBDZClMQ7uidx%5CVcxZlpwd0iXWU0oNI8%5CU4TusZwygeR689N833po4%2B%2BVHGWwqzb%3A1715163058080; o_act=login; ref_source=other_https://www.zhihu.com/knowledge-plan/hot-question/hot/0/day; expire_in=15552000; q_c1=6b48e9160f474705b13c906c5c0946aa|1715162167000|1715162167000; tst=r; BEC=43d4532fd57f0c3c659e43172114057d; z_c0=2|1:0|10:1715162170|4:z_c0|92:Mi4xMlJxOUZBQUFBQUFBY0JjbFRIbkZGaGNBQUFCZ0FsVk5OcG9vWndEMHFoMXJ1VjRQMXpfYkhKZ0RvYmZDYXUwY3RB|05099a3453c24f26dd3f65398ce25e70fb1f785ef7350bd8287b629318247631; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1715162235; KLBRSID=53650870f91603bc3193342a80cf198c|1715162236|1715162120",
    "referer": "https://www.zhihu.com/search?type=content&q=^%^E8^%^8B^%^B9^%^E6^%^9E^%^9C^",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": None
}

# 问题URL列表
questions = []
questionUrls = []

articles = []
articleUrls = []

def getPureTitle(title: str)->str:
    return title.replace("<em>", "").replace("</em>", "")

# 解析关键词搜索页获得数据
def parse(content: json):
    # 解析获取这一页的问题URL
    dataLst = content['data']
    for data in dataLst:
        if data['type'] != 'search_result':
            continue
        object = data['object']
        # 如果是问题
        if object['type'] == 'answer':
            question = object['question']
            print(f"index: {data['index']}, type: question, title: {getPureTitle(question['name'])}")
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
            print(f"index: {data['index']}, type: article, title: {getPureTitle(article['title'])}")
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


# 根据关键词检索获得问题URL
def getQuestionUrls(keyWord: str) -> None:
    page = 0
    search_hash_id = None
    pageSize = 20
    # 每次循环获取一页数据(20个问题/文章)，直到没有数据
    while page < 3:
        if page == 0:
            params = {
                "gk_version": "gz-gaokao",
                "t": "general",
                "q": keyWord,
                "correction": "1",
                "offset": str(page * pageSize),
                "limit": str(pageSize),
                "filter_fields": "",
                "lc_idx": str(page * pageSize),
                "show_all_topics": "0",
                "search_source": "Normal",
            }
        else:
            params = {
                'gk_version': 'gz-gaokao',
                't': 'general',
                'q': keyWord,
                'correction': '1',
                'offset': str(page * pageSize),
                'limit': str(pageSize),
                'filter_fields': '',
                'lc_idx': str(page * pageSize),
                'show_all_topics': '0',
                'search_hash_id': search_hash_id,
                'search_source': 'Normal',
                'vertical_info': f'0,1,0,0,0,0,0,0,0,{page * 4}',
            }

        # 完整请求路径
        fullUrl = f"{baseUrl}?{urlencode(params)}"
        # 知乎加密参数
        x_zse = execjs.compile(func).call('ed', fullUrl.replace('https://www.zhihu.com', ""))
        headers["X-Zse-96"] = f"2.0_{x_zse}"
        # 请求
        response = requests.get(fullUrl, headers=headers)

        # 检查响应状态码
        if response.status_code != 200:
            print(f"请求失败 url: {fullUrl}, text: {response.text}")
            break

        # 解析JSON内容
        content = json.loads(response.content.decode('utf-8'))

        # 如果后续没有数据，退出循环
        if content['paging']['is_end']:
            print(f"关键词 {keyWord} 爬取完毕")
            break

        parse(content)

        page += 1
        search_hash_id = content['search_action_info']['search_hash_id']

        print(f"paging : {content['paging']}, search_hash_id: {search_hash_id}")
        time.sleep(random.randint(2,5))

def saveQuestionsAndArticleToPath() -> None:
    with open(questionPath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=questions[0].getFieldName())
        writer.writeheader()  # 写入列名
        for question in questions:
            # 转换实体为字典，以便csv.DictWriter处理
            entity_dict = question.__dict__
            # 可以在这里添加额外的逻辑来清理或转换数据
            writer.writerow(entity_dict)
    print(f"问题数量：{len(questions)}")

    with open(articlePath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=articles[0].getFieldName())
        writer.writeheader()  # 写入列名
        for article in articles:
            # 转换实体为字典，以便csv.DictWriter处理
            entity_dict = article.__dict__
            # 可以在这里添加额外的逻辑来清理或转换数据
            writer.writerow(entity_dict)
    print(f"文章数量：{len(articles)}")

    with open('../data/qustion_urls.txt', 'w', encoding='utf-8') as f:
        for questionUrl in questionUrls:
            f.write(questionUrl+"\n")


if __name__ == '__main__':
    with open('x96.js', 'r', encoding='utf-8') as f:
        func = f.read()
    getQuestionUrls('人工智能')
    saveQuestionsAndArticleToPath()
