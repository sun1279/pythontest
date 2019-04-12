#this case is used to check whether a proxy is working or not
#some free proxy websites
#http://free-proxy.cz/zh/proxylist/country/CN/all/ping/all
#http://www.freeproxylists.net/zh/
import requests
import re
import sys
import threading

name_len = len(sys.argv)

headers = {
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
BAIDU='https://www.baidu.com/s?wd=ip'

OKlist=list()
'''
ip format 8.8.8.8:8080
'''
def check_proxy(ip):
    URL='http://'+ip
    S_URL='https://'+ip
    proxies1={
    'http': URL,
    'https': S_URL,
    }
    try:
        t=requests.get(BAIDU, proxies=proxies1, headers=headers,timeout=25)
        if t.status_code is 200:
            OKlist.append(ip)
            print(ip+'  OK')
            return True
    except:
        print(ip+'  NG')
        return False

def check_proxy_list(IpList):
    print("Createing thread...")
    for ip in IpList:
        check_proxy(ip)
    

ThreadNum=20

def get_proxy_list_by_threadnum(IpList, threadnum, cur_num):
    i=0
    l=len(IpList)
    l1=list()
    cur=cur_num*(l/threadnum)
    #print("cur {}".format(cur))
    #print("cur {}".format(cur+(l/threadnum)))
    for ip in IpList:
        if i < cur:
            i+=1
            continue
        if i < (cur+(l/threadnum)):
            l1.append(ip)
        i+=1
    return l1

with open('proxy_list.txt') as fd:
        Iplist=fd.read()
Iplist=Iplist.split('\n')

threads=list()
for j in range(ThreadNum):
    iplist=get_proxy_list_by_threadnum(Iplist, ThreadNum, j)
    t=threading.Thread(target=check_proxy_list, args=(iplist,))
    threads.append(t)
    t.start()

for t in threads:
        t.join()

for ok in OKlist:
    print(ok)
