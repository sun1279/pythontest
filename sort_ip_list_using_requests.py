#get ip infomation using request.get
import urllib2
import requests 
import time 
import sys
import json

url="http://ip-api.com/json/"
ip="8.8.8.8"

#r=requests.get("http://ip-api.com/json/8.8.8.8")
def ip_to_country(ip):
    time.sleep(0.9)
    try:#in case connection reset by peer
        r=requests.get(url+ip)
    except:
        return "UNKOWN"
    print(r.json()['status'])
    if r.json()["status"] == "fail":
        return r.json()["status"]
    else:
        return r.json()['country']



f_ip = open("sort_by_ip.txt", "r+")
f_cn = open("sort_by_cn.txt", "r+")
f = open("ip.txt", 'r')
words = []
for line in f:
    words.append(line)
words.sort()
for word in words:
    pass

print "=============================================="
cnt = 0;
cn_total = []
i = 0
flag = 0
a=dict()
b=dict()
l=list()
m=list()
for c in words:
    a[c]=a.get(c,0) + 1


for ip, num in list(a.items()):#this is key 
    l.append((num, str(ip)))

l.sort(reverse=True)
for num, ip in l:
    ip=ip.strip()
    print(ip)
    print(num)
    f_ip.write(str(ip))
    i=len(str(ip))
    while i < 20:
        f_ip.write(" ")
        i+=1
    f_ip.write(str(num))
    f_ip.write("\n")
    
f_ip.close()
#print(a.items())
for num, ip in l:
    print("IP",ip),
    country=ip_to_country(ip.strip())#must use strip here if use reuqests to get country
    print(country.encode('utf8'))
    if country not in b:
        b[country]=num
    else:
        b[country]+=num

for cn,num in list(b.items()):
    m.append((num, cn))

m.sort(reverse=True)
for num, cn in m:
#    try:
#    	f_cn.write(str(cn))
#    except:
#    	f_cn.write("Unknown")
    print(cn.encode('utf8')),
    print(str(num))
    f_cn.write(cn.encode('utf8'))#some names of country not encode well
    l=len(cn.encode('utf8'))
    print(cn.encode('utf8'))
    i = l
    while i < 20:
        f_cn.write(" ")
        i+=1
    f_cn.write(str(num))
    print(str(num))
    f_cn.write("\n")
    #print(cn),
    #print(num)

#f_ip.close()
f_cn.close()
f.close()
