import requests
import re
import sys
import threading
import time

from requests_html import HTMLSession


headers = {
        'Referer': 'https://www.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
URL='http://114.hisense.com/smtel/search/listview.do?depnum=hisense'
URL_PRE='http://114.hisense.com/smtel/search/listview.do?depnum='

session = HTMLSession()

fd=open('All.csv','w+')

def get_dep_only_info(r):
    qs=r.html
    js=qs.find('.listcontent')
    ks=js[0].find('tbody')[0]
    js=ks.find('.tip')
    l=list()
    print(len(js))
    for i in range(len(js)):
        if 'showuser' in js[i].html:
            print()
            fd.write('\n')
            str_tmp=re.findall('\'(.*)\'', js[i].html)[0]
            print(str_tmp+'@hisense.com', end=' ')#username
            fd.write(str_tmp+'@hisense.com,')
        print(js[i].text,end=' ')
        fd.write(js[i].text+',')
    print()
    fd.write('\n')


def check_type(r):
    qs=r.html
    t=qs.find('.listcontent')[0].text
    if '+86' in t:
        print("only user")
        return 1
    else:
        print("combine or Only dep")
        return 2

dep_code=list()

def get_dep_info(depname):
    time.sleep(5)
    r = session.get(URL_PRE+depname, headers=headers)
    check = check_type(r)
    if check == 2:
        qs=r.html
        qs=qs.find('.tip')
        if qs:
            cnt=0
            for q in qs:
                if 'depnum' in q.html:
                    print()
                    title=q.text
                    s=q.html.split('depnum=')[1]
                    code=re.findall('(.*)\"', s)[0]
                    print(title)
                    print(code)
                    dep_code.append(code[0])
                    get_dep_info(code)
                else:
                    if 'showuser' in q.html:
                        print()
                        fd.write('\n')
                        str_tmp=re.findall('\'(.*)\'', q.html)[0]
                        fd.write(str_tmp+'@hisense.com'+',')
                        print(str_tmp+'@hisense.com', end=' ')#username
                    print(q.text,end=' ')
                    fd.write(q.text+',')
                cnt+=1
        print()
        fd.write('\n')
    else:
        print('Only List')
        get_dep_only_info(r)


get_dep_info('dmt')
fd.close()

