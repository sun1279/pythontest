from flask import Flask,render_template
from flask import request
import requests
import json

URL="http://bskj.qdtcn.com:8088/pos/pay/queryBalanceByShowCardId"
URL1="http://bskj.qdtcn.com:8088/pos/pay/queryBalanceByShowCardId?cardId="
cardNo = "3104930400000368767"
#URL1+=cardNo
p={"cardId":cardNo}
#p={"cardId":cardNo, "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://www.qdtcn.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"}
#r=requests.post(URL1)
#wb=r.json()
#print(wb['balance'])

app = Flask(__name__)

@app.route('/showdict', methods=['GET'])
def showdict():
    number = request.args.get('number')
    if len(number) < 16:
        price = 'error'
    else:
        URL1="http://bskj.qdtcn.com:8088/pos/pay/queryBalanceByShowCardId?cardId="
        print(URL1)
        URL1+=number
        r=requests.post(URL1)
        wb=r.json()
        price = wb['balance']
        print(price)

    return render_template("showdict.html", number=number,price=price)



@app.route('/', methods=['POST', 'GET'])
def dict_form():
    if request.method == "POST":
        number = request.form['number']
        return redirect(url_for('showdict', number=number))
    return render_template("dict.html")

if __name__ =="__main__":
    app.run(debug=True, port=39003, host='0.0.0.0')
