import hashlib
import execjs
from urllib.parse import quote

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-api-version': '3.0.91',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_5KcY6+pyb96B4BbWLB1GG5Qtp6DUvzQZS6+crUkSGRn=ZzASW9WHNK5t8D1In0cG',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZKTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHgG3wNKjuCMbXxx_CgqHhL9AhV_pU2O9hVYPuYYEbH8S_pLgwXGvgNqyUoTveeXFBL1i9OqWqx0D9oBtgwCxUeqJrc1JvXBcJx1mUcCqhw9SGL8twHBpggffJNCHckLJqCL87Hmxg91b_3siGgYBHw1xgg82woxpg3CEuc90D9_VGpsOqfzwhwYLcSY8wxf9CCmqGt0Lbg0VwNBxg3McULyXhUC3UefFBVGWDCOcHHMbMc_oMF9gCL8qcrVjCNmFbNBhqpOpgrfr8NBehLBYHX1QqLfahx_WwXCqrSC',
}

def getSignature(params:str)->str:
    with open('g_encrypt.js', 'r') as f:
        ctx = execjs.compile(f.read())
        signature = ctx.call('D', hashlib.md5(params.encode("utf-8")).hexdigest())
        print(f"params: {params}, signature: {signature}")
        return signature
def process(keyword:str)->None:
    keyword=quote(keyword)
    ses=requests.session()
    url='https://www.zhihu.com/search?type=content&q={keyword}'.format(keyword=keyword)
    response=ses.get(url, headers=headers, timeout=20)
    print(response.cookies.values(), response.headers, response.status_code,sep='\n')
    cookie_dc0="ALBU2ZcilhePTrLjK5IA1cOhFMf6zwRoPlc=|1697992389" # response.cookies.get('d_c0','')
    params=f"101_3_3.0+/api/v4/search_v3?gk_version=gz-gaokao&t=general&q={keyword}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+{cookie_dc0}"
    x_zse_96=getSignature(params)
    headers.update({"x-zse-96":f"2.0_{x_zse_96}"})
    url=f'https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q={keyword}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal'
    response=ses.get(url, headers=headers, timeout=20)
    print(response.json())

if __name__ == '__main__':
    process('人工智能')
