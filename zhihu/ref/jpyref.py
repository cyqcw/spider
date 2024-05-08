from urllib import parse
import hashlib
import subprocess
import requests
import urllib.parse


class zhihu_v3():
    def __init__(self):
        self.url = "https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal" #相关api

    def call_js_x_s(self, func_name, *args):
        with open(r'cnsec.js', 'r') as f:
            js_code = f.read().strip()
        # 构造要执行的 JS 代码字符串
        js_args = [f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args]
        js_func_call = f"{func_name}({', '.join(js_args)})"
        js_complete_code = f"{js_code};nconsole.log({js_func_call});"
        # 使用 Node.js 执行 JS 代码，并将 stdout 存储到 res 变量中
        res = subprocess.run(['node', '-e', js_complete_code], capture_output=True, text=True)
        # 输出函数返回结果
        return res.stdout.strip()

    def get_headers(self):
        host = 'https://www.zhihu.com'
        en_url = urllib.parse.quote(self.url.replace(host, ''), safe='/?~()*!&=.\'')
        f = "+".join(['101_3_3.0', en_url, '"AKCdgpPR0hSPTnWADvuo2iMwzm_RhcN8G-s=|1650525184"'])
        fmd5 = hashlib.new('md5', f.encode()).hexdigest()
        encrypt_str = "2.0_%s" % self.call_js_x_s('D', fmd5)
        headers = {
            'x-app-za': 'OS=Web',
            "x-zse-93": "101_3_3.0",
            "x-zse-96": encrypt_str,
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Cookie": "_zap=0e195c0c-98b9-4a14-aa13-6121ae2c74cd; d_c0=ALBU2ZcilhePTrLjK5IA1cOhFMf6zwRoPlc=|1697992389; __snaker__id=olApQtmhiwbmpeyX; _xsrf=NDWkyb0gZvkQFH8ABcYYX87T5wMz0G4o; q_c1=4cdd7e30e6a34f3ba66b2834adbe5613|1713582633000|1713582633000; z_c0=2|1:0|10:1713582742|4:z_c0|92:Mi4xMlJxOUZBQUFBQUFBc0ZUWmx5S1dGeGNBQUFCZ0FsVk5LSUFRWndDVnFhZldWMi1zVThRYk14YjVIYVNuOVhaXzZ3|950cf96b0e1e4ea6e0e77724c71210d40e7ec4f45bff922e578a29f29a7a7633; gdxidpyhxdE=4%2FL%5C4dOnkuuVizqagsXEWBvWH%2FVk4GIO7S9fXJlaCMWb3r%5ColdAmp%5CSNE2x3K9vnKUqt8JUvD9Kel7c0naOlePc66KHJzRSOy5hMVavRmZJ38MjQUt8%5CKYmclUulJbZz03CbOo%2FGOXtqE8hXgN%2Fc6%5CysHLWvUPmvN12%2BHo3o6TVSGYwc%3A1714208638670; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1714015142,1714037265,1714186028,1714381984; tst=r; SESSIONID=lF1RMlWVKLvxvHTowKaULSUIFShdajd6u4ewn65yBii; JOID=W1oWBkli5pctnjzRTm62zy_Y6EtTBaGgeNhbhx4ioeBT73-OIPIYr0eeNtZPsaYzQos_96eaXsXPXizTjABWz9o=; osd=Vl8cCkxv450hmzHURGKzwirS5E5eAKusfdVejRInrOVZ43qDJfgUqkqbPNpKvKM5To4y8q2WW8jKVCDWgQVcw98=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1715093270; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1715098087|1715098028"  # 自己的cookie值,
        }
        self.zh_ask(headers)

    def zh_ask(self, headers):
        resp = requests.get(url=self.url, headers=headers)
        print(resp.text)

def start():
    op.get_headers()


if __name__ == '__main__':
    op = zhihu_v3()
    start()