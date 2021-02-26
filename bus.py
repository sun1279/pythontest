#http://127.0.0.1:8888/login?name=xiaoming&pwd=111111
import requests
import flask, json
from flask import request
 
def get_bus_list(num, station):
    URL="http://bus.qingdaonews.com/m/detail_ajax.php?rid={rid}&smid={rid}&id={id}&from=m".format(rid=num, id=station)
    try:
        r=requests.get(URL)
        print(r)
        print(r.json())
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


'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
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

    print(num)
    print(station)
    wb=get_bus_list(num, station)
    print(wb)
    bus_info=""
    if 'status' in wb[0].keys():
        resu = [{'bus': wb[0]['status']}]
        return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
    else:
        for w in wb:
            a=w['current_station_name']+"  "+w['time_to_there']+"\n还有"+w['station_count_remain']+"站\n"
            bus_info+=a
            resu = {'bus': bus_info}
        if len(wb) == 1: #only one on the road
            return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
            
        tmp=int(wb[1]['station_count_remain'])
        new_station=int(station)-tmp
    
        wb=get_bus_list(num, new_station)
        print(wb)
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

    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    #if username and pwd:
    #    if username=='xiaoming' and pwd=='111':
    #        resu = {'code': 200, 'message': '登录成功'}
    #        return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
    #    else:
    #        resu = {'code': -1, 'message': '账号密码错误'}
    #        return json.dumps(resu, ensure_ascii=False)
    #else:
    #    resu = {'code': 10001, 'message': '参数不能为空！'}
    #    return json.dumps(resu, ensure_ascii=False)
 
if __name__ == '__main__':
    server.run(debug=True, port=39000, host='0.0.0.0')
