# Description: 定义知乎数据实体类
import json


# 知乎问题实体类
class Question:
    def __init__(self, id: str, type: str, name: str,
                 url: str, answerCount: int, followCount: int):
        self.id = id
        self.type = type
        self.name = name
        self.url = url
        self.answerCount = answerCount
        self.followCount = followCount

    def __str__(self):
        # 使用json.dumps将对象转换为JSON格式的字符串，确保中文等非ASCII字符被正确处理
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)

    def __repr__(self):
        return f'{self.id},{self.type},{self.name},{self.url},{self.answerCount},{self.followCount}'

    @classmethod
    def getFieldName(cls):
        return ['id', 'type', 'name', 'url', 'answerCount', 'followCount']


# 知乎回答实体类
class Answer:
    def __init__(self, id: str, questionId: str, questionTitle: str, authorId: str, author: str,
                 authorUrl: str, authorType: str, authorHeadline: str,
                 type: str, url: str, excerpt: str, voteupCount: int,
                 commentCount: int, favoriteCount: int, createdTime: str,
                 updatedTime: str, content: str):
        self.id = id
        self.questionId = questionId
        self.questionTitle = questionTitle
        self.authorId = authorId
        self.author = author
        self.authorUrl = authorUrl
        self.authorType = authorType  # 作者类型
        self.authorHeadline = authorHeadline  # 作者简介
        self.type = type
        self.url = url
        self.excerpt = excerpt  # 摘要
        self.voteupCount = voteupCount  # 赞同数
        self.commentCount = commentCount  # 评论数
        self.favoriteCount = favoriteCount  # 收藏数
        self.createdTime = createdTime
        self.updatedTime = updatedTime
        self.content = content

    def __str__(self):
        # 使用json.dumps将对象转换为JSON格式的字符串，确保中文等非ASCII字符被正确处理
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)

    def __repr__(self):
        return f'{self.id},{self.questionId},{self.questionTitle},{self.authorId},{self.author},{self.authorUrl},{self.authorType},{self.authorHeadline},{self.type},{self.url},{self.excerpt},{self.voteupCount},{self.commentCount},{self.favoriteCount},{self.createdTime},{self.updatedTime},{self.content}'

    @classmethod
    def getFieldName(cls):
        return ['id', 'questionId', 'questionTitle', 'authorId', 'author', 'authorUrl', 'authorType',
                'authorHeadline', 'type', 'url', 'excerpt', 'voteupCount', 'commentCount', 'favoriteCount',
                'createdTime', 'updatedTime', 'content']


# 知乎文章实体类
class Article:
    def __init__(self, id: str, authorId: str, author: str, authorUrl: str,
                 authorType: str, authorHeadline: str, title: str, type: str,
                 url: str, excerpt: str, voteupCount: int, commentCount: int,
                 zfavCount: int, createdTime: str, updatedTime: str, content: str):
        self.id = id
        self.authorId = authorId
        self.author = author
        self.authorUrl = authorUrl
        self.authorType = authorType  # 作者类型
        self.authorHeadline = authorHeadline  # 作者简介
        self.title = title
        self.type = type
        self.url = url
        self.excerpt = excerpt
        self.voteupCount = voteupCount
        self.commentCount = commentCount
        self.zfavCount = zfavCount
        self.createdTime = createdTime
        self.updatedTime = updatedTime
        self.content = content

    def __str__(self):
        # 使用json.dumps将对象转换为JSON格式的字符串，确保中文等非ASCII字符被正确处理
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)

    def __repr__(self):
        return f'{self.id},{self.authorId},{self.author},{self.authorUrl},{self.authorType},{self.authorHeadline},{self.title},{self.type},{self.url},{self.excerpt},{self.voteupCount},{self.commentCount},{self.zfavCount},{self.createdTime},{self.updatedTime},{self.content}'

    @classmethod
    def getFieldName(cls):
        return ['id', 'authorId', 'author', 'authorUrl', 'authorType', 'authorHeadline',
                'title', 'type', 'url', 'excerpt', 'voteupCount', 'commentCount',
                'zfavCount', 'createdTime', 'updatedTime', 'content']


# 类和类型转换器
ClassTypeTransfer = {
    Question: "问题",
    Answer: "回答",
    Article: "文章",
    "问题": Question,
    "回答": Answer,
    "文章": Article
}
