import csv
import os
import random
import execjs
import requests
import json
import time
from urllib.parse import urlencode

from entity import *
from config import *
from utils import *

params = {
    'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled',
    'offset': None,
    'limit': None,
    'sort_by': 'default',
    'platform': 'desktop'
}

def parseAnswer(content: json, answers: list) -> None:
    dataLst = content['data']
    for data in dataLst:
        print(f"正在解析，问题：{data['question']['id']}，答案：{data['id']}")
        answers.append(
            Answer(
                data['id'], data['question']['id'], cleanWebContent(data['question']['title']), data['author']['id'], data['author']['name'],
                data['author']['url'], data['author']['user_type'], data['author']['headline'],
                data['type'], data['url'], data['excerpt'], data['voteup_count'],
                data['comment_count'], None, data['created_time'],
                data['updated_time'], cleanWebContent(data['content'])
        ))

def getAllAnswers(questionUrl: str) -> None:
    start = 0
    limit = 20
    while True:
        # 每一页保存一次
        answers = []
        print(f"正在爬取第{start // limit}页数据")
        params['offset'] = start
        params['limit'] = limit
        # 完整请求路径
        fullUrl = f"{questionUrl}?{urlencode(params)}"
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
        parseAnswer(content, answers)
        # 保存一页的回答到文件中
        saveEntitiesToPath(answers, answerPath, ClassTypeTransfer.get(Answer))
        start += limit
        if content['paging']['is_end']:
            print(f"爬取了此问题下的所有数据 共 {content['paging']['totals']}条")
            break
        time.sleep(random.Random().randint(2, 5))

if __name__ == '__main__':
    with open(questionPath, 'r', encoding='utf-8') as f:
        f.readline()
        lines = f.readlines()
        ids = [line.split(',')[0] for line in lines][34:]
        print(ids)
        for id in ids:
            getAllAnswers(f'https://www.zhihu.com/api/v4/questions/{id}/answers')
