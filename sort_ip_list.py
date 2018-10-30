#This sorts the IP list by times 
#alse sort by ip location
# Version1
# need to be optimized
#from __future__ import print_function
import urllib2
import time 
import sys
import json
def ip_to_country(ip):
    y = {}
    x = {}
    for y in urllib2.urlopen(ip,timeout=1):#on some machine, timeout=1 is a must or it will stop here
        pass
    x = json.loads(y)
#    print x
    time.sleep(0.5)
    if "fail" in y:
	return x["status"]
    else:
        return x["country"]



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
    l.append((num, ip))

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
    
addr_pre = 'http://ip-api.com/json/'
#print(a.items())
for num, ip in l:
    country = ip_to_country(addr_pre+ip)
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

f_ip.close()
f_cn.close()
f.close()
