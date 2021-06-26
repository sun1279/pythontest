#get lowest price of each day within 3 mmonths
#get flight and price of one special day
import json
import time
import requests
import sys
import random
from fake_useragent import UserAgent
ua = UserAgent()

headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'User-Agent': ua.random,
    'X-Requested-With': 'XMLHttpRequest',
}



CTRIP_URL1='https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?'
CTRIP_URL2='https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258'
CTRIP_URL3 ='https://m.ctrip.com/restapi/soa2/13515/routeSale?_fxpcqlniredt=09031058414411692501'
CTRIP_URL4='https://m.ctrip.com/restapi/soa2/19728/getPersonalizedTheme?_fxpcqlniredt=09031134314362678836'
CTRIP_URL5='https://m.ctrip.com/restapi/soa2/13515/airportCityList?_fxpcqlniredt=09031028414387203028'

CTRIP_JSON_NAME='ctrip_city.json'


class Ctrip(object):
    def __init__(self):
        self.__date__  = ''
        self.__dcity__ = ''
        self.__acity__ = ''
    def __update_city_list__(self):
        '''update json file, which contains dicts of city&IATA code'''

        self.__chr_list__ = list()
        self.__city_json__ = dict()
        for c in range(65,91):
            self.__chr_list__.append(chr(c))
        self.__chr_list__.remove('I')
        self.__chr_list__.remove('O')
        self.__chr_list__.remove('U')
        self.__chr_list__.remove('V')
            
        '''get all citys by Initials'''
        for c in self.__chr_list__:
            p={"q":1,"intial":c,"b":2,"head":{"cid":"09031028414387203028","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":"66672"},{"name":"sid","value":"1693366"},{"name":"protocal","value":"https"}]},"contentType":"json"}
            r = requests.post(CTRIP_URL5, data=json.dumps(p), headers=headers)
            wb=r.json()
            alllist = wb['pl'][0]['cl']
            for l in alllist:
                self.__city_json__[l['name']] = l['code']
            time.sleep(5)
        with open(CTRIP_JSON_NAME,'w') as fd:
            json.dump(self.__city_json__, fd)

    def __input2iata__(self, input_city):
        '''City name to IATA'''
        with open(CTRIP_JSON_NAME) as fd:
            wb = json.load(fd)
        if input_city in wb.keys():
            return wb[input_city]
        else:
            return ''

    def get_flights_by_city(self, dep, arr):
        '''lowest price between 2 cities everyday for the nearest 3 months'''
        self.__dcity__ = self.__input2iata__(dep)
        self.__acity__ = self.__input2iata__(arr)
        p={"stype":1,"dCty":self.__dcity__,"aCty":self.__acity__,"flag":'',"start":"","end":"","head":{"cid":"","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":""},{"name":"sid","value":""},{"name":"protocal","value":"https"}]},"contentType":"json"}
        r=requests.post(CTRIP_URL1, data=json.dumps(p),headers=headers)
        wb=r.json()
        ls=wb['prices']
        return ls

    def get_flights_by_day(self, dep, arr, date):
        '''all flights between 2 cities on a specified day'''
        self.__dcity__ = self.__input2iata__(dep)
        self.__acity__ = self.__input2iata__(arr)
        p={"preprdid":"","trptpe":1,"flag":8,"searchitem":[{"dccode":self.__dcity__,"accode":self.__acity__,"dtime":date}],"subchannel":'',"tid":"{6d549c74-62d5-42e7-a2cb-35c94d349df4}","head":{"cid":"09031046111774300258","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"protocal","value":"https"}]},"contentType":"json"}
        r=requests.post(CTRIP_URL2, data=json.dumps(p), headers=headers)
        wb=r.json()
        #print(wb)
        all_flight= wb.get('fltitem')
        return all_flight

    def get_flights_by_qd(self):
        '''get destinations by discount from qingdao '''
        request_0={"departureCityCode":"TAO","tripType":"S","head":{"cid":"09031058414411692501","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":"66672"},{"name":"sid","value":"1693366"},{"name":"protocal","value":"https"}]},"contentType":"json"}
        CTRIP_URL3 ='https://m.ctrip.com/restapi/soa2/13515/routeSale?_fxpcqlniredt=09031058414411692501'
        r = requests.post(CTRIP_URL3, data=json.dumps(request_0), headers=headers)
        wb=r.json()
        r_list = wb['routes']
        return r_list
        for i in r_list:
            print(i)
    def get_flights_by_qd1(self):
        '''get destinations from qingdao '''
        request_1={"dCityCode":"TAO","tripType":1,"moreDays":1,"head":{"cid":"09031134314362678836","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":"66672"},{"name":"sid","value":"1693366"},{"name":"protocal","value":"https"}]},"contentType":"json"}
        r = requests.post(CTRIP_URL4, data=json.dumps(request_1), headers=headers)
        print(r)
        print(r.json())
        wb=r.json()
        s_list=wb['srlt']
        return s_list
        for s in s_list:
            typr=s['hlPrices']
            for t in typr:
                print(t)

if __name__ == '__main__':
    myctrip = Ctrip()
    #myctrip.update_city_list()
    #a=myctrip.get_flights_by_qd()
    #a=myctrip.get_flights_by_city('青岛','北京')
    #print(a)
    #for l in a:
    #    print(l.get('airname'),end='  ')
    #    print(l.get('flightNo').ljust(7),end='  ')
    #    print(l.get('dDate'),end='   ')
    #    print(l.get('dweek'),end=' ')
    #    print(l.get('price'))


   # a=myctrip.get_flights_by_day('青岛','北京','2021-07-01')
   # for l in a:
   #     print(l.get('mutilstn')[0].get('basinfo').get('flgno').ljust(8), end='     ')
   #     print(l.get('mutilstn')[0].get('dportinfo').get('cityname'),end='(')
   #     print(l.get('mutilstn')[0].get('dportinfo').get('aportsname'),end=')    ')
   #     print(l.get('mutilstn')[0].get('aportinfo').get('cityname'), end='(')
   #     print(l.get('mutilstn')[0].get('aportinfo').get('aportsname'), end=')    ')
   #     data=l.get('mutilstn')[0].get('dateinfo').get('ddate')
   #     print(data.split()[0],end='     ')
   #     print(data.split()[1],end='     ')
   #     data=l.get('mutilstn')[0].get('dateinfo').get('adate')
   #     print(data.split()[1],end='     ')
   #     print(l.get('policyinfo')[0].get('priceinfo')[0].get('price'), end='    ')
   #     print(l.get('mutilstn')[0].get('craftinfo').get('cname'), end='')
   #     print(l.get('mutilstn')[0].get('craftinfo').get('craft'))
    a=myctrip.get_flights_by_qd()
    for i in a:
        print(i)
   # a=myctrip.get_flights_by_qd1()
   # for s in a:
   #         typr=s['hlPrices']
   #         for t in typr:
   #             print(t)


