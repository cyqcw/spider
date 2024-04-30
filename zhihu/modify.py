url="https://api.zhihu.com/search_v3?advert_count=0&correction=1&filter_fields=&gk_version=gz-gaokao&lc_idx=0&limit=20&offset=20&q=人工智能&search_hash_id=6a2fa2d5ebf923cb22d062a7e2ca6ef6&search_source=Normal&show_all_topics=0&t=general&vertical_info=0,1,0,0,0,0,0,0,0,0"


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
    "X-Zse-96": "2.0_t8AqDH=tPzk2NKV3L5WdhSktS12DwDqcwB2Xqam7Dnh5SSrASZJUZlRI=2r5J7f1"
}

# 查询参数
params = {
    "gk_version": "gz-gaokao",
    "t": "general",
    "q": "人工智能",
    "correction": "1",
    "offset": "0",
    "limit": "20",
    "filter_fields": "",
    "lc_idx": "0",
    "show_all_topics": "0",
    "search_source": "History"
}

import requests
import json

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print("请求失败", response.status_code, response.text)
