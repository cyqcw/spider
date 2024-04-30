from baiduspider import BaiduSpider
from pprint import pprint

spider = BaiduSpider()

pprint(spider.search_zhidao(query="人工智能").plain)