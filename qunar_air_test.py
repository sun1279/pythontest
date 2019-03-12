import json
import requests
import sys
headers = {
    'origin': 'https://m.flight.qunar.com',
    'd70e3d': '24ff1efc086fb6a3dcc9c5e676728a14',
    'content-type': 'application/json',
    'Referer': 'https://m.flight.qunar.com/ncs/page/flightlist?depCity=%E5%8C%97%E4%BA%AC&arrCity=%E4%B8%8A%E6%B5%B7&goDate=2019-03-12&from=touch_index_search&child=0&baby=0&cabinType=0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


cmd_len=len(sys.argv)
if cmd_len is not 4:
    print('Usage: python3 air_test.py 青岛 北京 2019-05-12')
    exit()
print(sys.argv[1], end='-')
print(sys.argv[2], end=' ')
print(sys.argv[3])
DepCity=sys.argv[1]
ArrCity=sys.argv[2]
Date=sys.argv[3]
p={"_firstScreen":"1","arrCity":"青岛","baby":"0","cabinType":"0","child":"0","depCity":"北京","from":"touch_index_search","goDate":"2019-03-15","firstRequest":True,"startNum":0,"sort":5,"r":1552373807281,"_v":2,"underageOption":"","__m__":"54059ef6ec01fbb774910bc59d0a2966"}
#p={"arrCity":ArrCity,"baby":"0","cabinType":"0","child":"0","depCity":DepCity,"from":"touch_index_search","goDate":Date,"firstRequest":True,"startNum":0,"sort":5,"r":1552300519937,"_v":2,"underageOption":"","__m__":"7155ada775d780fc49777c9f0ff89765"}

r=requests.post('https://m.flight.qunar.com/flight/api/touchInnerList', data=json.dumps(p), headers=headers)
wb=r.json()
#print(r.url)
all_flight=wb.get('data').get('flights')
i=0

print('航班号   出发机场  到达机场       日期     起飞时间  落地时间   最低票价')
for l in all_flight:
    if l.get('binfo'):
        #print(l.get('binfo'))
        print(l.get('binfo').get('airCode'), end='  ')
        print(l.get('binfo').get('depCity'), end='(')
        print(l.get('binfo').get('depAirport'), end=')-')
        print(l.get('binfo').get('arrCity'), end='(')
        print(l.get('binfo').get('arrAirport'), end=')  ')
        print(l.get('binfo').get('date'),end='    ')
        print(l.get('binfo').get('depTime'),end='     ')
        print(l.get('binfo').get('arrTime'),end='     ')
        print(l.get('minPrice'))
    else:
        break
