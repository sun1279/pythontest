import json
import requests
import sys
import random

URL='http://103.230.35.222:3128'
S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https

URL1='62.152.43.152:8080'
S_URL1='62.152.43.152:8080'
URL2='43.243.165.206:3128'
S_URL2='43.243.165.206:3128'
URL3='77.59.248.61:8080'
S_URL3='77.59.248.61:8080'
URL4=URL3
S_URL4=S_URL3
URL5='139.255.123.186:8080'
S_URL5='139.255.123.186:8080'
URL6='202.138.243.8:8080'
S_URL6='202.138.243.8:8080'

proxy_pool={
        6:{'http': URL2, 'https': S_URL2},
        5:{'http': URL1, 'https': S_URL1},
        4:{'http': URL2, 'https': S_URL2},
        3:{'http': URL3, 'https': S_URL3},
        2:{'http': URL4, 'https': S_URL4},
        1:{'http': URL5, 'https': S_URL5},
        0:{'http': URL6, 'https': S_URL6},
        }


headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
#    'Referer': 'https://m.ctrip.com/html5/flight/swift/domestic/BJS/SHA/2019-04-15',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
#p={"stype":1,"dCty":"TAO","aCty":"BJS","flag":'',"start":"","end":"","head":{"cid":"09031046111774300258","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":"66672"},{"name":"sid","value":"1693366"},{"name":"protocal","value":"https"}]},"contentType":"json"}
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


print(code_name)
if cmd_len is not 4:
    print('Usage: python3 air_test.py 青岛 北京 0/1')
    exit()
print(sys.argv[1], end='-')
print(sys.argv[2], end=' ')
DepCity=code_name.get(sys.argv[1])
ArrCity=code_name.get(sys.argv[2])
Sort=sys.argv[3]
print(DepCity, end=' ')
print(ArrCity, end=' ')
Sort=int(Sort)


p={"stype":1,"dCty":DepCity,"aCty":ArrCity,"flag":'',"start":"","end":"","head":{"cid":"","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":"66672"},{"name":"sid","value":"1693366"},{"name":"protocal","value":"https"}]},"contentType":"json"}
#r=requests.post('https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258', data=json.dumps(p), headers=headers)
serv_id = random.randint(0,6)
#r=requests.post('https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?', data=json.dumps(p),headers=headers, proxies=proxy_pool.get(serv_id%6))
#wb=r.json()
#save_wb_to_file(wb, "wb.txt")
wb=get_wb_from_file('wb.txt')
#print(wb)
ls=wb['prices']
price_d=dict()
for l in ls:
    if Sort is 0:
        print(l.get('airname'),end='  ')
        print(l.get('flightNo').ljust(7),end='  ')
        print(l.get('dDate'),end='   ')
        print(l.get('dweek'),end=' ')
        print(l.get('price'))
    price_d[l.get('airname')+'  '+l.get('flightNo').ljust(6) + '   '+l.get('dDate')+'   '+l.get('dweek') ]=l.get('price')
    

if Sort is not 0:
    for w in sorted(price_d, key=price_d.get):
        print (w, price_d[w])
