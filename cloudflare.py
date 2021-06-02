import requests
import json
import time
URL_ALL_DOMAINS="https://api.cloudflare.com/client/v4/zones/"
URL_1_DOMAIN="https://api.cloudflare.com/client/v4/zones/{}/dns_records"
headers={"Content-Type":"application/json", "X-Auth-Key":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "X-Auth-Email":"xxxxxx@gmail.com"};
my_domains=['xxxxx.cn', 'xxxxxx.xyz', 'xxxxxx.xxxx']

class Mycloudflare(object):
    def __init__(self):
        self.__domain_dict__={}
        self.__sub_domain_dict__={}
        self.__domain_all_list__=[]
        r=requests.get(URL_ALL_DOMAINS, headers=headers)
        info=r.json()['result']
        for i in info:
            self.__domain_dict__[i['name']]=i['id']
            r=requests.get(URL_1_DOMAIN.format(i['id']), headers=headers)
            #print(r.json())
            if r.json()['success'] is not True:
                exit()
            result=r.json()['result']
            self.__domain_all_list__.append(result)
            for d in result:
                self.__sub_domain_dict__[d['name']]=d['id']
        #print(self.__domain_all_list__)

    def getallinfo(self):
        return self.__domain_all_list__

    def cadd(self, subdomain, ip, proxied):
        new_domain = subdomain
        new_ip =ip
        new_proxied = proxied 
        zone_name=new_domain.split('.')[-2]+'.'+new_domain.split('.')[-1]
        try:
            zone_id=self.__domain_dict__[zone_name]
        except:
            print("Domain error\n")
            exit(0)
        URL_DNS="https://api.cloudflare.com/client/v4/zones/{}/dns_records".format(zone_id)
        data={"type":"A","name":new_domain,"content":new_ip,"ttl":1,"proxied":new_proxied}
        r=requests.post(URL_DNS, headers=headers, data=json.dumps(data))
        print(r.json())
        if r.json()['success'] is True:
            self.__sub_domain_dict__[new_domain]=r.json()['result']['id']
        return r.json()

    def cdel(self, subdomain):
        d_domain=subdomain
        zone_name=d_domain.split('.')[-2]+'.'+d_domain.split('.')[-1]
        zone_id=self.__domain_dict__[zone_name]
        try:
            sub_id=self.__sub_domain_dict__[d_domain]
        except:
            print("Domain not found\n")
            exit(0)
        print(zone_id)
        print(sub_id)
        URL_DEL="https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}".format(zone_id, sub_id)
        print(URL_DEL)
        r=requests.delete(URL_DEL, headers=headers)
        return r.json()

if __name__ == '__main__':
    myc=Mycloudflare()
    myc.cadd("cfffffffffffffffffffff.xxxxxx.xyz","1.1.1.x", False)
    time.sleep(2)
    myc.cdel("xxx.xxxxxx.xyz")
    exit()

