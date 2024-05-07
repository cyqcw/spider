import json
import requests

xza96=[
    "2.0_5KcY6+pyb96B4BbWLB1GG5Qtp6DUvzQZS6+crUkSGRn=ZzASW9WHNK5t8D1In0cG",
    "2.0_a7UQaXYUhs5s/1c+f6vrP10xhiQRBj19FrI6rQwzItJXyB+5uqePIsecmuUu1Kn4",
    "2.0_/5/CjkOf3rBNyXLAtuSXsKPoZC6LWKYdISi9MLpcIxsIPMFKAwS/65tMS1I658wf"
]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-api-version': '3.0.91',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_5KcY6+pyb96B4BbWLB1GG5Qtp6DUvzQZS6+crUkSGRn=ZzASW9WHNK5t8D1In0cG',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZKTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHgG3wNKjuCMbXxx_CgqHhL9AhV_pU2O9hVYPuYYEbH8S_pLgwXGvgNqyUoTveeXFBL1i9OqWqx0D9oBtgwCxUeqJrc1JvXBcJx1mUcCqhw9SGL8twHBpggffJNCHckLJqCL87Hmxg91b_3siGgYBHw1xgg82woxpg3CEuc90D9_VGpsOqfzwhwYLcSY8wxf9CCmqGt0Lbg0VwNBxg3McULyXhUC3UefFBVGWDCOcHHMbMc_oMF9gCL8qcrVjCNmFbNBhqpOpgrfr8NBehLBYHX1QqLfahx_WwXCqrSC',
}

cookies = {
    '_zap': '0e195c0c-98b9-4a14-aa13-6121ae2c74cd',
    'd_c0': 'ALBU2ZcilhePTrLjK5IA1cOhFMf6zwRoPlc=|1697992389',
    '__snaker__id': 'olApQtmhiwbmpeyX',
    '_xsrf': 'NDWkyb0gZvkQFH8ABcYYX87T5wMz0G4o',
    'q_c1': '4cdd7e30e6a34f3ba66b2834adbe5613|1713582633000|1713582633000',
    'z_c0': '2|1:0|10:1713582742|4:z_c0|92:Mi4xMlJxOUZBQUFBQUFBc0ZUWmx5S1dGeGNBQUFCZ0FsVk5LSUFRWndDVnFhZldWMi1zVThRYk14YjVIYVNuOVhaXzZ3|950cf96b0e1e4ea6e0e77724c71210d40e7ec4f45bff922e578a29f29a7a7633',
    'gdxidpyhxdE': '4%2FL%5C4dOnkuuVizqagsXEWBvWH%2FVk4GIO7S9fXJlaCMWb3r%5ColdAmp%5CSNE2x3K9vnKUqt8JUvD9Kel7c0naOlePc66KHJzRSOy5hMVavRmZJ38MjQUt8%5CKYmclUulJbZz03CbOo%2FGOXtqE8hXgN%2Fc6%5CysHLWvUPmvN12%2BHo3o6TVSGYwc%3A1714208638670',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1714015142,1714037265,1714186028,1714381984',
    'tst': 'r',
    'SESSIONID': 'NJQdqK0BUk68p3oa3DJce9JTTRWawxSg4k39gMIIxoo',
    'JOID': 'VF4XBk3HPjR3FFuub8RuYnFXgDR8iXBiEGUQmiqSVQZIZ2jBCqCqABIUX61rudGnl_a6HFXdB8pg0Yw2dRqEdtw=',
    'osd': 'VVwWA0LGPDVyG1qsbsFhY3NWhTt9i3FnH2QSmy-dVARJYmfACKGvDxMWXqhkuNOmkvm7HlTYCMti0Ik5dBiFc9M=',
    'BEC': '43d4532fd57f0c3c659e43172114057d',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1714466211',
    'KLBRSID': 'fe0fceb358d671fa6cc33898c8c48b48|1714466211|1714460510',
}


params = {
    'gk_version': 'gz-gaokao',
    't': 'general',
    'q': '人工智能',
    'correction': '1',
    'offset': '0',
    'limit': '20',
    'filter_fields': '',
    'lc_idx': '0',
    'show_all_topics': '0',
    'search_source': 'Normal',
}

headers['x-zse-96'] = xza96[0]
response = requests.get('https://www.zhihu.com/api/v4/search_v3', params=params, cookies=cookies, headers=headers)
content = json.loads(response.content.decode('utf-8'))
print(content['paging']['next'])

headers['x-zse-96'] = xza96[1]
params = {
    'gk_version': 'gz-gaokao',
    't': 'general',
    'q': '人工智能',
    'correction': '1',
    'offset': '20',
    'limit': '20',
    'filter_fields': '',
    'lc_idx': '20',
    'show_all_topics': '0',
    'search_hash_id': 'fe1f2c52bc245466a7714c890869324c',
    'search_source': 'Normal',
    'vertical_info': '0,1,0,0,0,0,0,0,0,0',
}

response = requests.get('https://www.zhihu.com/api/v4/search_v3', params=params, cookies=cookies, headers=headers)
content = json.loads(response.content.decode('utf-8'))
print(content['paging']['next'])

headers ['x-zse-96'] = xza96[2]

params = { # 有顺序
    'gk_version': 'gz-gaokao',
    't': 'general',
    'q': '人工智能',
    'correction': '1',
    'offset': '40',
    'limit': '20',
    'filter_fields': '',
    'lc_idx': '40',
    'show_all_topics': '0',
    'search_hash_id': 'fe1f2c52bc245466a7714c890869324c',
    'search_source': 'Normal',
    'vertical_info': '0,1,0,0,0,0,0,0,0,0',
}

response = requests.get('https://www.zhihu.com/api/v4/search_v3', params=params, cookies=cookies, headers=headers)
content = json.loads(response.content.decode('utf-8'))
print(content['paging']['next'])