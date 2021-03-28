import requests
import json

URL="http://bskj.qdtcn.com:8088/pos/pay/queryBalanceByShowCardId"
URL1="http://bskj.qdtcn.com:8088/pos/pay/queryBalanceByShowCardId?cardId="
cardNo = "3104930400000368767"
URL1+=cardNo
p={"cardId":cardNo}
#p={"cardId":cardNo, "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://www.qdtcn.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"}
r=requests.post(URL1)
wb=r.json()
print(wb['balance'])
