import requests
#GET /m/detail_ajax.php?rid=643&smid=643&id=36&from=m HTTP/1.1
headers={
'Host': 'bus.qingdaonews.com',
'Connection': 'keep-alive',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Referer': 'http://bus.qingdaonews.com/m/detail.html?rid=643',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

r=requests.get("http://bus.qingdaonews.com/m/detail_ajax.php?rid=643&smid=643&id=36&from=m", headers=headers)
print(r)
print(r.json())

URL="http://bus.qingdaonews.com/m/detail.php?rid=643&isjson=1"
r=requests.get(URL, headers=headers)
print(r)
print(r.json())
