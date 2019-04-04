import json
import requests
import sys
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


if cmd_len is not 3:
    print('Usage: python3 air_test.py 青岛 北京 ')
    exit()
print(sys.argv[1], end='-')
print(sys.argv[2], end=' ')
DepCity=code_name.get(sys.argv[1])
ArrCity=code_name.get(sys.argv[2])
#Date=sys.argv[3]
print(DepCity)
print(ArrCity)
#print(Date)


p={"stype":1,"dCty":DepCity,"aCty":ArrCity,"flag":'',"start":"","end":"","head":{"cid":"","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":"66672"},{"name":"sid","value":"1693366"},{"name":"protocal","value":"https"}]},"contentType":"json"}
#r=requests.post('https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258', data=json.dumps(p), headers=headers)
r=requests.post('https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?', data=json.dumps(p),headers=headers)
wb=r.json()
print(wb)
ls=wb['prices']
for l in ls:
    print(l.get('airname'),end=' ')
    print(l.get('flightNo'),end=' ')
    print(l.get('dDate'),end=' ')
    print(l.get('dweek'),end=' ')
    print(l.get('price'))
