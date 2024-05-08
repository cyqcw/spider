import requests
import execjs



'''
#获取知乎评论的内容
    需要替换自己的cookie
'''


with open('x96.js','r',encoding='utf-8') as f:
    func = f.read()

url = "https://www.zhihu.com/api/v4/comment_v5/answers/3308302434/root_comment?order_by=score&limit=20&offset="


x_zse = execjs.compile(func).call('ed',url.replace('https://www.zhihu.com',""))

## 替换自己的cookie
headers = {
    "authority": "www.zhihu.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "",
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
    "x-zse-96": f"2.0_{x_zse}"
}

response = requests.get(url, headers=headers)

print(response.text)
print(response)