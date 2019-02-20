#this case is used to check whether a proxy is working or not
#some free proxy websites
#http://free-proxy.cz/zh/proxylist/country/CN/all/ping/all
#http://www.freeproxylists.net/zh/
import requests
import re
import sys
#proxies1={'http': 'http://103.230.35.222:3128'}
URL='http://103.230.35.222:3128'
S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https
#URL='http://104.248.126.17:8080'
#S_URL='https://104.248.126.17:8080'

name_len = len(sys.argv)

if name_len > 1:
    URL='http://'+sys.argv[1]
    S_URL='https://'+sys.argv[1]
else:
    print("Usage:")
    print("      python3 proxy_test.py 104.248.126.17:8080" )
    exit()

def get_orig_ip(long_url):
    ip = URL.split(':')[1][2:]
    return ip

proxies1={
'http': URL,
'https': S_URL,
}

headers = {
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
BAIDU='https://www.baidu.com/s?wd=ip'
try:
    t=requests.get(BAIDU, proxies=proxies1, headers=headers)
except:
    print("requests error, maybe proxy not in service")
    exit()
all_list=t.content.decode().split('=')
l=list()
l1=list()
for l in all_list:
    if '本机' in l and 'c-gap-right' in l:
        l1=l

s1=str(l1).split()
s2=re.findall('IP\S+', str(s1[0]))
str1=str(s2[0])[:3]
l2=str(s2[0])[9:].split('</span>')
str2=l2[0]+ ' ' +l2[1]
print(str2)
if l2[0] != get_orig_ip(URL):
    print("ERROR, Using Proxy Faild!!!")

