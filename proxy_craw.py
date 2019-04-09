#craw one page of proxies from xicidaili.com
from requests_html import HTMLSession
session = HTMLSession()
proxies1={
        'http': '103.230.35.222:3128',
        'https':'103.230.35.222:3128',
        }

headers = {
        'Referer': 'https://www.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
r = session.get('https://www.xicidaili.com/nt/', proxies=proxies1, headers=headers)
t=r.html
o=t.find('tr')
iplist=list()
for i in o:
    if '时间' not in i.html:
        iplist.append(i.html.split('<td>')[1].split('</td>')[0]+':'+i.html.split('<td>')[2].split('</td>')[0])
        #print(i.html.split('<td>')[1].split('</td>')[0],end=':')
        #print(i.html.split('<td>')[2].split('</td>')[0])

with open('proxy_list.txt','w+') as fd:
    for ip in iplist:
        fd.write(ip+'\n')

print("Ip list saved to proxy_list.txt")

