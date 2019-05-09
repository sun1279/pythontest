# coding=utf8
from requests_html import HTMLSession
import time
import json

session = HTMLSession()
headers = {
#'Referer': 'https://www.baidu.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}
URL='http://www.gcmap.com/airport/'

def GetInfoByIATA(code):
    try:
        r=session.get(URL+code, headers=headers)
    except:
        exit()
    q=r.html
    t=q.find('table')[2].text
    t=t.split('\n')
    t.pop(0)
    cnt = 10
    l1=list()
    l2=list()
    l1=t[::2]
    l2=t[1::2]
    d=dict()
    for i in range(10):
        d[l1[i][:-1]] = l2[i]

    return d

cities=list()
with open('InternationalAirCode.json') as fd:
    cities=json.load(fd)

for city in cities:
    code=city['tcode']
    #print(code)
    retd=GetInfoByIATA(code)
    try:
        city['ICAO']=retd['ICAO']
    except:
        city['ICAO']=''
    try:
        city['Latitude']=retd['Latitude']
        city['Longitude']=retd['Longitude']
    except:
        pass
    print(',',end='')
    print(retd)
    time.sleep(40)
print(cities)
