import csv
import os
from bs4 import BeautifulSoup
import re
from entity import *
from config import *

# 清洗网页内容
def cleanWebContent(content: str)->str:
    # 使用BeautifulSoup移除HTML标签
    soup = BeautifulSoup(content, 'lxml')
    text = soup.get_text()

    # 删除多余空白字符（包括换行符、制表符等），并压缩多个空格为一个
    cleanedText = re.sub(r'\s+', ' ', text).strip()
    return cleanedText

# 保存实体到文件
def saveEntitiesToPath(entities: list, path: str, _type: str)->bool:
    try:
        # 写入列名
        if not os.path.isfile(path):
            with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=ClassTypeTransfer.get(_type).getFieldName())
                writer.writeheader()
        # 写入数据
        with open(path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=ClassTypeTransfer.get(_type).getFieldName())
            for entity in entities:
                entity_dict = entity.__dict__
                writer.writerow(entity_dict)
        print(f"成功保存{_type}数量：{len(entities)}")
        return True
    except:
        return False

# 获得已经爬取过的Url
def getAlreadyUrls() -> list:
    # TODO: 读取已经爬取过的URL
    with open(questionPath, 'r', encoding='utf-8') as qu, \
            open(articlePath, 'r', encoding='utf-8') as au:
        return [line.strip() for line in au.readlines()]

# 读出加密函数
with open('x96.js', 'r', encoding='utf-8') as f:
    func = f.read()