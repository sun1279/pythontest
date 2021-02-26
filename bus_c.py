#http://127.0.0.1:8888/login?name=xiaoming&pwd=111111
import requests
import flask, json
from flask import request
 
#station info http://bus.qingdaonews.com/m/detail.php?rid=643&isjson=1

S_NAME="current_station_name"
COUNT="station_count_remain"
TIME="time_to_there"
DIRECT="station_direct"

class Bus(object):
    def __init__(self, num):
        self.__num__ = num
        self.__seg_id__ = 0
        URL="http://bus.qingdaonews.com/m/detail.php?rid={rid}&isjson=1".format(rid=self.__num__)
        try:
           r=requests.get(URL)
           if r.status_code == 200:
               if type(r.json()) is dict:#normal-list abnormal-dict
                   self.__seg_id__ = r.json()['stations'][0]['segment_id']
        except:
            pass
     



    def get_bus_list(self, station):
       URL="http://bus.qingdaonews.com/m/detail_ajax.php?rid={rid}&smid={smid}&id={id}&from=m".format(rid=self.__num__, smid=self.__seg_id__, id=station)
       try:
           r=requests.get(URL)
    #       print(r.json())
           if r.status_code == 200:
               if type(r.json()) is list:#normal-list abnormal-dict
                   return r.json()
               else:
                   if 'status' in r.json().keys():
                       return [{'status':r.json()['status']}]
                   if 'error' in r.json().keys():
                       return [{'status':r.json()['error']}]
           else:
               return [{'status':'Failed0'}]
       except:
               return [{'status':'Unkown Error'}]
     
    def get_bus_info(self):
        URL="http://bus.qingdaonews.com/m/detail.php?rid={rid}&isjson=1".format(rid=self.__num__)
        try:
           r=requests.get(URL)
           if r.status_code == 200:
               if type(r.json()) is list:
                   return {'status':'Failed0'}
               else:
                   return r.json()["bus_info"]
           else:
               return {'status':'Failed0'}
        except:
               return {'status':'Unkown Error'}
    def get_name_by_station(self, station):
        URL="http://bus.qingdaonews.com/m/detail.php?rid={rid}&isjson=1".format(rid=self.__num__)
        try:
           r=requests.get(URL)
           if r.status_code == 200:
               if type(r.json()) is list:
                   return "Known0"
               else:
                   return r.json()["stations"][station-1]['station_name']
           else:
                return "Known1"
        except:
                return "Known2"
    def get_all_bus(self):
        URL="http://bus.qingdaonews.com/m/detail.php?rid={rid}&isjson=1".format(rid=self.__num__)
        try:
           r=requests.get(URL)
           if r.status_code == 200:
               if type(r.json()) is list:
                   return "Known0"
               else:
                   stations=r.json()["stations"]
           else:
                return "Known1"
        except:
                return "Known2"
        total=len(stations)
        mtcnt = 0
        mocnt = 0
        for s in stations:
            if s[DIRECT] == "MT":
                mtcnt+=1
            if s[DIRECT] == "MO":
                mocnt+=1
        #print(mtcnt, mocnt)
        total -= 1;
        wb = self.get_bus_list(total)
        offset = 1
        bus_info_mt=''
        bus_info_mo=''
        mt_list=list()
        mo_list=list()

        print("MO {} -> {}".format(stations[mtcnt]['station_name'], stations[total]['station_name']))
        print("MT {} -> {}".format(stations[0]['station_name'], stations[mtcnt-1]['station_name']))
        while (len(wb) == 2):
            if 'status' in wb[0].keys():
                break;
            else:
                for w in wb:
                    tmp_dict=dict()
                    a=w[S_NAME]+"  "+w[TIME]+"\n"
        #            print(a)
                    tmp_dict[S_NAME]=w[S_NAME]
                    tmp_dict[TIME]=w[TIME]
                    if total > mtcnt:
                        if((total-int(w[COUNT])) <  mtcnt):
                            mt_list.append(tmp_dict)
                            bus_info_mt+=a
                        else:
                            mo_list.append(tmp_dict)
                            bus_info_mo+=a
                    else:
                        mt_list.append(tmp_dict)
                        bus_info_mt+=a
                    #print(bus_info)
            tmp=int(wb[1]['station_count_remain'])
            total = total - tmp
            #print("GET {}".format(total))
            #print("Get {}".format(total))
            wb = self.get_bus_list(total)

        out_dict=dict()
        #print(mt_list)
        #print(mo_list)
        out_dict["mt"]=mt_list
        out_dict["mo"]=mo_list
        return out_dict

        #print(stations[0])
        #print(stations[mtcnt-1])
        #print(stations[mtcnt])
        #print(stations[total-1])
        print(bus_info_mt)
        print("====================")
        print("{} -> {}".format(stations[0]['station_name'], stations[mtcnt-1]['station_name']))
        print(bus_info_mo)




# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    # 获取通过url请求传参的数据
    num = request.values.get('num')
    # 获取url请求传的密码，明文
    station= request.values.get('station')
    bus=Bus(num)
    wb=bus.get_all_bus()
    print(wb)
    exit()
    wb=bus.get_bus_list(station)
    print(wb)
    bus_info=''
    if 'status' in wb[0].keys():
        resu = [{'bus': wb[0]['status']}]
        return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
    else:
        for w in wb:
            a=w[S_NAME]+"  "+w[TIME]+"\n还有"+w[COUNT]+"站\n"
            bus_info+=a
            print(bus_info)
            resu = {'bus': bus_info}
        if len(wb) == 1: #only one on the road
            return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
        
        tmp=int(wb[1]['station_count_remain'])
        new_station=int(station)-tmp
        wb=bus.get_bus_list(new_station)
        if 'status' in wb[0].keys():
            resu = [{'bus': wb[0]['status']}]
            resu = {'bus': bus_info}
            return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
        else:
            for w in wb:
                new_remain=int(w['station_count_remain'])+tmp
                a=w['current_station_name']+"  "+w['time_to_there']+"\n还有"+str(new_remain)+"站\n"
                bus_info+=a
            resu = {'bus': bus_info}
         
        return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
      
    
if __name__ == '__main__':
    server.run(debug=True, port=39000, host='0.0.0.0')
