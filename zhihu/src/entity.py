# Description: 定义知乎数据实体类

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
        return f"问题：{self.name}，URL：{self.url}，回答数：{self.answerCount}, 关注者数：{self.followCount}"

    def __repr__(self):
        return f'{self.id},{self.type},{self.name},{self.url},{self.answerCount},{self.followCount}'


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
        return f"作者：{self.author}, 赞同数：{self.voteupCount}, 内容：{self.content}"

    def __repr__(self):
        return f'{self.id},{self.questionId},{self.questionTitle},{self.authorId},{self.author},{self.authorUrl},{self.authorType},{self.authorHeadline},{self.type},{self.url},{self.excerpt},{self.voteupCount},{self.commentCount},{self.favoriteCount},{self.createdTime},{self.updatedTime},{self.content}'

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
        return f"作者：{self.author}, 赞同数：{self.voteupCount}, 内容：{self.content}"

    def __repr__(self):
        return f'{self.id},{self.authorId},{self.author},{self.authorUrl},{self.authorType},{self.authorHeadline},{self.title},{self.type},{self.url},{self.excerpt},{self.voteupCount},{self.commentCount},{self.zfavCount},{self.createdTime},{self.updatedTime},{self.content}'
