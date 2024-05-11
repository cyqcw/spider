import random
import execjs
import requests
import time
from urllib.parse import urlencode

from utils import *

# 目标接口
baseUrl = "https://www.zhihu.com/api/v4/search_v3"

# 解析一页关键词搜索得到的数据
def parseQuestionAndArticle(content: json, questions: list, articles: list, alreadyUrls: list)->None:
    # 解析获取这一页的问题URL
    dataLst = content['data']
    for data in dataLst:
        if data['type'] != 'search_result':
            print(f"非搜索返回类型：{data['type']}!")
            continue
        object = data['object']
        # 如果是问题，知乎一般是返回问题的一个回答
        if object['type'] == 'answer':
            question = object['question']
            print(f"{data['index']}, question, {cleanWebContent(question['name'])}")
            # 如果问题URL不在列表中,也不在已爬取的列表中,添加到列表
            if question['url'] not in alreadyUrls:
                questions.append(Question(
                    question['id'], question['type'], cleanWebContent(question['name']),
                    question['url'], question['answer_count'], question['follow_count']
                ))
                alreadyUrls.append(question['url'])
        # 如果是文章
        elif object['type'] == 'article':
            article = object
            print(f"{data['index']}, article, {cleanWebContent(article['title'])}")
            # 如果文章URL不在列表中，添加到列表
            if article['url'] not in alreadyUrls:
                articles.append(
                    Article(
                        article['id'], article['author']['id'], cleanWebContent(article['author']['name']),
                        article['author']['url'], article['author']['type'], cleanWebContent(article['author']['headline']),
                        cleanWebContent(article['title']), article['type'], article['url'], cleanWebContent(article['excerpt']),
                        article['voteup_count'], article['comment_count'], article['zfav_count'],
                        article['created_time'], article['updated_time'], cleanWebContent(article['content'])
                ))
                alreadyUrls.append(article['url'])
        else:
            print(f"非目标类型：{object['type']} !")

# 根据关键词检索获得问题URL
def getQuestionAndArticleFromKeyword(keyWord: str, alreadyUrls: list) -> None:
    page = 0
    search_hash_id = None
    pageSize = 20
    # 每次循环获取一页数据(20个问题/文章)，直到没有数据
    while True:
        questions = []
        articles = []

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

        print(f'正在爬取关键词：{keyWord}，第{page+1}页，{fullUrl}')
        # 知乎加密参数
        x_zse = execjs.compile(func).call('ed', fullUrl.replace('https://www.zhihu.com', ""))
        headers["X-Zse-96"] = f"2.0_{x_zse}"
        # 请求
        response = requests.get(fullUrl, headers=headers)

        # 检查响应状态码
        if response.status_code != 200:
            print(f"请求失败! 关键词: {keyword}, page: {page+1}, url: {fullUrl}, text: {response.text}")
            break

        # 解析JSON内容
        content = json.loads(response.content.decode('utf-8'))

        # 从关键词搜索页面中解析出问题和文章
        parseQuestionAndArticle(content, questions, articles, alreadyUrls)

        # 保存一页的问题和文章到文件中
        saveEntitiesToPath(questions, questionPath, ClassTypeTransfer.get(Question))
        saveEntitiesToPath(articles, articlePath, ClassTypeTransfer.get(Article))

        # 迭代进入下一次循环
        page += 1
        search_hash_id = content['search_action_info']['search_hash_id']

        # 如果后续没有数据，退出循环
        if content['paging']['is_end']:
            print(f"关键词 {keyWord} 爬取完毕, 共{page}页")
            break

        time.sleep(random.randint(2,5))

if __name__ == '__main__':
    # 获取已经爬取过的URL
    alreadyUrls = getAlreadyUrls()

    # 爬取关键词对应的问题和文章
    for keyword in keyWords:
        getQuestionAndArticleFromKeyword(keyword, alreadyUrls)