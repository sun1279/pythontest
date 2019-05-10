# coding=utf8
from requests_html import HTMLSession
import time
import json
import sqlite3

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
    print(r.status_code)
    q=r.html
    t=q.find('table')[2].text
    t=t.split('\n')
    t.pop(0)
    l1=list()
    l2=list()
    l1=t[::2]
    l2=t[1::2]
    if len(l1) > len(l2):
        l1.pop(len(l1)-1)
    elif len(l1) < len(l2):
        l2.pop(len(l2)-1)
    else:
        pass
    d=dict()
    for i in range(len(l1)):
        d[l1[i][:-1]] = l2[i]
    return d

cities=list()
with open('InternationalAirCode.json') as fd:
    cities=json.load(fd)

con=sqlite3.connect('air.sqlite')
cur=con.cursor()
try:
    cur.execute("SELECT * from aircode")
except:
    sql_cmd="""CREATE TABLE aircode (icao varchar(4), iata varchar(3));"""
    cur.execute(sql_cmd)




for city in cities:
    code=city['tcode']
    sqlcode=(code,)
    cur.execute('SELECT * FROM aircode WHERE iata=?',sqlcode)
    s=cur.fetchone()
    if s:#ICAO already in DB
        city['ICAO']=s[0]
    else:
        print(code+" not in Database")
        retd=GetInfoByIATA(code)
        try:
            city['ICAO']=retd['ICAO']
        except:
            city['ICAO']=''
        if len(city['ICAO']) is 0 or len(city['ICAO']) is 4:
            sql_command = "INSERT INTO aircode (icao, iata) VALUES (?,?)"
            cur.execute(sql_command, (city['ICAO'],city['tcode']))
            con.commit()
        try:
            city['Latitude']=retd['Latitude']
            city['Longitude']=retd['Longitude']
        except:
            pass
        print(',',end='')
        print(retd)
        time.sleep(30)

print(len(cities))
with open('InternationalAirCode.json','w') as fd:
    json.dump(cities, fd)
con.close()
