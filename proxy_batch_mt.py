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
        t=requests.get(BAIDU, proxies=proxies1, headers=headers,timeout=18)
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
    

ThreadNum=15


'''This function saperates the Total ip list to several small lists based on number of threads'''
#param1 list of all the ips
#param2 No. of thread left
#param3 current lenth of Iplist
def get_proxy_list_by_threadnum(IpList, threadnum, cur_len):
    i=0
    l1=list()
    #if there is only one thread
    if threadnum is 1:
        return IpList
    else:
        cur=cur_len//threadnum
        for ip in IpList:
            if i < cur:
                l1.append(ip)
                Iplist.remove(ip)
            i+=1

    return l1

with open('proxy_list.txt') as fd:
        Iplist=fd.read()
Iplist=Iplist.split('\n')

llen=len(Iplist)
#in case there in empty element in the list
if not Iplist[llen-1]:
    Iplist.pop(llen-1)

threads=list()
#remove duplicates from original list
Iplist=list(set(Iplist))

#see if Thread number is larger than Ip number
if len(Iplist) < ThreadNum:
    ThreadNum=len(Iplist)

i=0
for j in range(ThreadNum):
    llen=len(Iplist)
    iplist=get_proxy_list_by_threadnum(Iplist, ThreadNum-j, llen)
    t=threading.Thread(target=check_proxy_list, args=(iplist,))
    threads.append(t)
    t.start()

for t in threads:
        t.join()

for ok in OKlist:
    print(ok)
