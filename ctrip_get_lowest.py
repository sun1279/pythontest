#get lowest price of each day within 3 mmonths
#get flight and price of one special day
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

MYcity=['澳门', '北京', '白山', '长春', '重庆', '长沙', '成都', '稻城', '大连', '大理', '敦煌', '广州', '贵阳', '桂林', '海口', '呼和浩特', '合肥', '杭州', '哈尔滨', '黄山', '九寨沟', '昆明', '兰州', '丽江', '拉萨', '林芝', '上海', '沈阳', '上饶', '三亚', '深圳', '武汉', '武夷山', '香格里拉', '香港', '西安', '厦门 ', '西宁', '银川', '延吉', '张家界', '珠海']

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
    r=requests.post('https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?', data=json.dumps(p),headers=headers, proxies=proxy_pool.get(serv_id%6))
    wb=r.json()
    ls=wb['prices']
    return ls
def PrintUsage(fname):
    print('Usage: python3 {} -A 青岛 北京(list low price each day within three months)'.format(sys.argv[0]))
    print('       python3 {} -D 青岛 北京 2019-05-01(list all flight of a specify day)'.format(sys.argv[0]))
    print('       python3 {} -R 青岛(random destnation low price)'.format(sys.argv[0]))

#print(code_name)
if cmd_len is not 4 and cmd_len is not 3 and cmd_len is not 5:
    PrintUsage(sys.argv[0])
    exit()

if not sys.argv[1].startswith('-'):
    PrintUsage(sys.argv[0])
    exit()
else:
    if len(sys.argv[1]) is not 2:
        PrintUsage(sys.argv[0])
        exit()

Option=sys.argv[1][1:]
if Option is 'A':
    if cmd_len is 4:
        print(sys.argv[2], end='-')
        print(sys.argv[3])
        DepCity=code_name.get(sys.argv[2])
        ArrCity=code_name.get(sys.argv[3])
        if not DepCity:
            print("出发城市输入错误")
            PrintUsage(sys.argv[0])
            exit()
        if not ArrCity:
            print("到达城市输入错误")
            PrintUsage(sys.argv[0])
            exit()
        ret=GetLowPriceList(DepCity, ArrCity)
        PrintPriceList(ret)
    else:
        PrintUsage(sys.argv[0])
        exit()

elif Option is 'D':
    if cmd_len is 5:
        print(sys.argv[2], end='-')
        print(sys.argv[3])
        DepCity=code_name.get(sys.argv[2])
        ArrCity=code_name.get(sys.argv[3])
        Date=sys.argv[4]
        if not DepCity:
            print("出发城市输入错误")
            PrintUsage(sys.argv[0])
            exit()
        if not ArrCity:
            print("到达城市输入错误")
            PrintUsage(sys.argv[0])
            exit()
        if len(Date) is not 10:
            print("日期输入错误")
            PrintUsage(sys.argv[0])
            exit()
        else:
            _data=Date.split('-')
            if len(_data) is not 3:
                print("日期输入错误")
                PrintUsage(sys.argv[0])
                exit()
        ret=GetPriceByDate(DepCity, ArrCity, Date)
        PrintPriceByDate(ret)
    else:
        PrintUsage(sys.argv[0])
        exit()
elif Option is 'R':
    if cmd_len is 3:
        print(sys.argv[2], end='-')
        DepCity=code_name.get(sys.argv[2])
        if not DepCity:
            print("出发城市输入错误")
            PrintUsage(sys.argv[0])
            exit()
    else:
        PrintUsage(sys.argv[0])
        exit()
else:
    PrintUsage(sys.argv[0])
    exit()

exit()

#    price_d=dict()
#    for l in ls:
#        price_d[l.get('airname')+'  '+l.get('flightNo').ljust(6) + '   '+l.get('dDate')+'   '+l.get('dweek') ]=l.get('price')
#
#    return price_d

 


#d=GetLowPriceListByDate(code_name.get(sys.argv[1]), code_name.get(sys.argv[2]))
#print(d)


'''
p={"stype":1,"dCty":DepCity,"aCty":ArrCity,"flag":'',"start":"","end":"","head":{"cid":"","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":""},{"name":"sid","value":""},{"name":"protocal","value":"https"}]},"contentType":"json"}

serv_id = random.randint(0,6)
r=requests.post('https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?', data=json.dumps(p),headers=headers, proxies=proxy_pool.get(serv_id%6))
wb=r.json()
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
'''
