#get lowest price of each day within 3 mmonths
#get flight and price of one special day
import json
import requests
import sys
import random

headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
#    'Referer': 'https://m.ctrip.com/html5/flight/swift/domestic/BJS/SHA/2019-04-15',
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


'''Print flight list a day'''

def PrintPriceByDate(ls):
    print('航班号         出发机场     到达机场        日期        起飞时间      落地时间   最低票价')
    for l in ls:
        print(l.get('mutilstn')[0].get('basinfo').get('flgno').ljust(8), end='     ')
        print(l.get('mutilstn')[0].get('dportinfo').get('cityname'),end='(')
        print(l.get('mutilstn')[0].get('dportinfo').get('aportsname'),end=')    ')
        print(l.get('mutilstn')[0].get('aportinfo').get('cityname'), end='(')
        print(l.get('mutilstn')[0].get('aportinfo').get('aportsname'), end=')    ')
        data=l.get('mutilstn')[0].get('dateinfo').get('ddate')
        print(data.split()[0],end='     ')
        print(data.split()[1],end='     ')
        data=l.get('mutilstn')[0].get('dateinfo').get('adate')
        print(data.split()[1],end='     ')
        print(l.get('policyinfo')[0].get('priceinfo')[0].get('price'))


'''Get the flight list and price a day, this return'''
def GetPriceByDate(dep, arr, date):
    p={"preprdid":"","trptpe":1,"flag":8,"searchitem":[{"dccode":dep,"accode":arr,"dtime":date}],"subchannel":'',"tid":"{6d549c74-62d5-42e7-a2cb-35c94d349df4}","head":{"cid":"09031046111774300258","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"protocal","value":"https"}]},"contentType":"json"}

    serv_id = random.randint(0,6)
    try:
        #r=requests.post('https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258', data=json.dumps(p), headers=headers, proxies=proxy_pool.get(serv_id%6))
        r=requests.post('https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258', data=json.dumps(p), headers=headers, )
    except:
        print("Error post")
        exit()
    wb=r.json()
    all_flight= wb.get('fltitem')
    return all_flight



'''Print lowest price within three months'''
def PrintPriceList(ls):
    for l in ls:
        print(l.get('airname'),end='  ')
        print(l.get('flightNo').ljust(7),end='  ')
        print(l.get('dDate'),end='   ')
        print(l.get('dweek'),end=' ')
        print(l.get('price'))

'''Get the Lowest price of every day within three months '''
def GetLowPriceList(dep, arr):
    p={"stype":1,"dCty":dep,"aCty":arr,"flag":'',"start":"","end":"","head":{"cid":"","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":""},{"name":"sid","value":""},{"name":"protocal","value":"https"}]},"contentType":"json"}
    serv_id = random.randint(0,6)
    print(serv_id)
    r=requests.post('https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?', data=json.dumps(p),headers=headers, )
    wb=r.json()
    ls=wb['prices']
    return ls
DepCity=code_name.get("青岛")
ArrCity=code_name.get("北京")
Date="2021-04-11"
ret=GetPriceByDate(DepCity, ArrCity, Date)
print(ret)

