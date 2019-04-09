#this case is used to check whether a proxy is working or not
#some free proxy websites
#http://free-proxy.cz/zh/proxylist/country/CN/all/ping/all
#http://www.freeproxylists.net/zh/
import requests
import re
import sys

name_len = len(sys.argv)

headers = {
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
BAIDU='https://www.baidu.com/s?wd=ip'

def get_orig_ip(long_url):
    ip = URL.split(':')[1][2:]
    return ip


with open('my_proxy.txt') as fd:
    Iplist=fd.read()
Iplist=Iplist.split('\n')
for ip in Iplist:
    print(ip)
    URL='http://'+ip
    S_URL='https://'+ip
    proxies1={
    'http': URL,
    'https': S_URL,
    }
    try:
        t=requests.get(BAIDU, proxies=proxies1, headers=headers,timeout=20)
    except:
        print("requests error, maybe proxy not in service")
        continue
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
    #on some cases, we can not get the real ip address we are using, NOT sure proxy is used correctly
    if l2[0] != get_orig_ip(URL):
        print("Using Proxy Failed")

