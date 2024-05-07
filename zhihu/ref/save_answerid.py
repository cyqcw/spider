import requests
import pandas as pd
import time

template = 'https://www.zhihu.com/api/v4/questions/30644408/feeds?cursor=1c4cacd45e70f24bd620bad51c605d59&include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled&limit=5&{offset}&order=default&platform=desktop&session_id=1698132896804376037'

df = pd.DataFrame()
# df有三列，answer_id和content以及创建日期
df['answer_id'] = []
df['content'] = []
df['created_time'] = []

answer_ids = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }

cookies = {
    "_zap": "0e195c0c-98b9-4a14-aa13-6121ae2c74cd",
    "d_c0": "ALBU2ZcilhePTrLjK5IA1cOhFMf6zwRoPlc=|1697992389",
    "__snaker__id": "olApQtmhiwbmpeyX",
    "_xsrf": "NDWkyb0gZvkQFH8ABcYYX87T5wMz0G4o",
    "q_c1": "4cdd7e30e6a34f3ba66b2834adbe5613|1713582633000|1713582633000",
    "z_c0": "2|1:0|10:1713582742|4:z_c0|92:Mi4xMlJxOUZBQUFBQUFBc0ZUWmx5S1dGeGNBQUFCZ0FsVk5LSUFRWndDVnFhZldWMi1zVThRYk14YjVIYVNuOVhaXzZ3|950cf96b0e1e4ea6e0e77724c71210d40e7ec4f45bff922e578a29f29a7a7633",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1714013395,1714015142,1714037265,1714186028",
    "gdxidpyhxdE": "7nvcDiSqXAGUK7kuD%2B%2BVM%2FgIcUW8to8rLN63vnYsdIdO7WrjR12MTLs2N3ezL4KkWVeTOlacubuum%2B%2FS4sAInoShwTdQ8yUNWTSwxBAKKAlGR%2FWvoKZalCgVr3P0PXi3%2B6Ph5HyVdP5qRC%2BgidxYr%5C2virbbMRxR%2BnX5IHRPszCfJnrU%3A1714202974017",
    "tst": "r",
    "SESSIONID": "5BfHoEg9iPxRIgJ12nubHBuhcM8ZzyRJlzFkgkyOZ0l",
    "JOID": "VV4UCkofCYDBAmdhHxFe1MtFsfwOK0zugWsjAS5wWP-bQwYqKfKprKkFYW4fbwG2fcsJA6zURMQsMfCfMlSbyHQ=",
    "osd": "WlAQCkIQB4TBCmhvGxFW28VBsfQBJUjuiWQtBS54V_GfQw4lJ_appKYLZW4XYA-yfcMGDajUTMsiNfCXPVqfyHw=",
    "KLBRSID": "ca494ee5d16b14b649673c122ff27291|1714206301|1714202070",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1714206302"
}

# 第一条使用模版，后面的都是next来获取
initUrl = template.format(offset=0)

resp0 = requests.get(initUrl, headers=headers, cookies=cookies)

print(resp0.json())

print(resp0.json()['data'])


# for data in resp0.json()['data']:
#         answer_id = data['target']['id']
#         answer_ids.append(answer_id)
# next = resp0.json()['paging']['next']

# for idx in range(1):# 这里自己估算一下，每页是5条数据
#     # 对第page页进行访问
#     resp = requests.get(next, headers=headers, cookies=cookies)
#     print(f'正在爬取第{idx}页')
    
#     for data in resp.json()['data']:
#         answer_id = data['target']['id']
#         # 添加answer_id到df中
#         answer_ids.append(answer_id)
#     next = resp.json()['paging']['next']
#     # time.sleep(1) # 这里是情况可快可慢

# # 将answer_ids写入df
# df['answer_id'] = answer_ids
# df.to_csv('answer_id.csv', index=True)




# from bs4 import BeautifulSoup
# import random
# contents = []
# batch = 0
# for answer_id in answer_ids:
#     print(f'正在爬取answer_id为{answer_id}的数据')
#     url = 'https://www.zhihu.com/question/30644408/answer/{answer_id}'.format(answer_id=answer_id)
#     try:
#         resp = requests.get(url, headers=headers, cookies=cookies)
#         soup = BeautifulSoup(resp.text, 'html.parser')
#         # 查找content
#         content = soup.find('div', class_='RichContent-inner').text
#         contents.append(content)
#         print(content)
#     except Exception as e:
#         print(f'爬取answer_id为{answer_id}的数据时出现异常：{e}')
#         break
    
#     # time.sleep(1)

#     # 每爬取100个回答就保存一次数据,保存在不同的文件中
    
#     if len(contents) % 100 == 0:
#         new_data = {'answer_id': answer_ids[:len(contents)], 'content': contents}
#         new_df = pd.DataFrame(new_data)
#         new_df.to_csv(f'text_{batch}.csv', index=True)
#         batch += 1

# # new_data = {'answer_id': answer_ids[:len(contents)], 'content': contents}
# # new_df = new_df.append(pd.DataFrame(new_data))
# # new_df.to_csv('text1.csv', index=True)

