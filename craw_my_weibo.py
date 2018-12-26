import requests
from urllib.parse import urlencode
#from pyquery import PyQuery

#mine#https://m.weibo.cn/api/container/getIndex?value=2680925293&page=1&containerid=1076032680925293
#https://m.weibo.cn/api/container/getIndex?value=2830678474&page=1&containerid=1076032830678474

max_page=100
page=1
url_prefix='https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2680925293',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

url_param={
"value":2680925293,
"containerid":1076032680925293,
"page":page

#"value":2830678474,
#"containerid":1076032830678474,
#"page":page
}

final_url=url_prefix+urlencode(url_param)
print(final_url)
try:
    response=requests.get(final_url, headers=headers)
    print(response.status_code)
#    print(response.json())
except:
    print("error")

txt=response.json()
print(type((txt.get('data'))))
#print((txt.get('data').get('mblog')))
l_data=txt.get('data').get('cards')
for index, data in enumerate(l_data):
    l_single_pic=list()
    #print(index),
    #print(data.get('mblog'))
    #continue
    if index is not 10000:
        if "raw_text" in data.get('mblog'):
            print("-----------转发微博---------")
            print(data.get('mblog').get('raw_text'))
            print("-----------转发内容---------")
            print(data.get('mblog').get('retweeted_status').get('text'))
            print("-----------原创用户---------")
            print(data.get('mblog').get('retweeted_status').get('user').get('screen_name'))
            continue
  
        else:
            print("-----------原创微博---------")
        print(data.get('mblog').get('text'))
        print("-----------转发数---------")
        print(data.get('mblog').get('reposts_count'))
        print("-----------评论数---------")
        print(data.get('mblog').get('comments_count'))
        if "pics" in data.get('mblog'):
            #    print(type(data.get('mblog').get('pics')))
                print(len(data.get('mblog').get('pics')))#number of pics
                l_data1=data.get('mblog').get('pics')
                for index1, data1 in enumerate(l_data1):
        #            print(index1),
                    l_single_pic.append(data1.get('large').get('url'))
        print(l_single_pic)
         
