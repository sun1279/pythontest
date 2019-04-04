import json
import requests
import sys
headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'Referer': 'https://m.ctrip.com/html5/flight/swift/domestic/BJS/SHA/2019-03-15',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
#save dict to file, in case we need that later
def save_wb_to_file(wb, filename):
    with open(filename,'w') as fd:
        json.dump(wb, fd)

#get dict back from file when needed
def get_wb_from_file(filename):
    with open(filename) as fd:
        return json.load(fd)


code_name=dict()
cmd_len=len(sys.argv)
wb=get_wb_from_file('addr_code')
ADDR=['ABCDEF','GHIJ','KLMN','PQRSTUVW','XYZ']
for addr in ADDR:
    #print(addr)
    w1=wb.get(addr)
    for c in  addr:
        if not w1.get(c):
            continue
        for l in w1.get(c):
            name=l.get('display')
            code=l.get('data')[-3:]
            code_name.update({name:code})


if cmd_len is not 4:
    print('Usage: python3 air_test.py 青岛 北京 2019-05-12')
    exit()
print(sys.argv[1], end='-')
print(sys.argv[2], end=' ')
print(sys.argv[3])
DepCity=code_name.get(sys.argv[1])
ArrCity=code_name.get(sys.argv[2])
Date=sys.argv[3]

#ArrCity="青岛"
#DepCity="南京"
#Date="2019-03-19"

p={"preprdid":"","trptpe":1,"flag":8,"searchitem":[{"dccode":DepCity,"accode":ArrCity,"dtime":Date}],"subchannel":'',"tid":"{6d549c74-62d5-42e7-a2cb-35c94d349df4}","head":{"cid":"09031046111774300258","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"protocal","value":"https"}]},"contentType":"json"}


r=requests.post('https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258', data=json.dumps(p), headers=headers)
wb=r.json()
#save_wb_to_file(wb,'ctrip.json')
#wb=get_wb_from_file('ctrip.json')

#print(r.url)
#print(r.headers)
#print(r.status_code)
#print(wb)
all_flight= wb.get('fltitem')
i=0

print('航班号         出发机场     到达机场        日期        起飞时间      落地时间   最低票价')
for l in all_flight:
    print(l.get('mutilstn')[i].get('basinfo').get('flgno').ljust(8), end='     ')
    print(l.get('mutilstn')[i].get('dportinfo').get('cityname'),end='(')
    print(l.get('mutilstn')[i].get('dportinfo').get('aportsname'),end=')    ')
    print(l.get('mutilstn')[i].get('aportinfo').get('cityname'), end='(')
    print(l.get('mutilstn')[i].get('aportinfo').get('aportsname'), end=')    ')
    data=l.get('mutilstn')[i].get('dateinfo').get('ddate')
    print(data.split()[0],end='     ')
    print(data.split()[1],end='     ')
    data=l.get('mutilstn')[i].get('dateinfo').get('adate')
    print(data.split()[1],end='     ')
    print(l.get('policyinfo')[i].get('priceinfo')[0].get('price'))


