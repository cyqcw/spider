# 关键词
keyWords = ['人工智能', 'AI', '大模型', '深度学习', '多模态', '自然语言处理', 'openai', 'chatgpt', 'deepmind']

# 保存路径
questionPath = '../data/questions.csv'
articlePath = '../data/articles.csv'
answerPath = '../data/answers.csv'

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