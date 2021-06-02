from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template
from flask import request
import json
import random

URL='https://www.scientificamerican.com/'
EXCLUDE=["https://www.scientificamerican.com/section/opinion/"]
headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

WEB1 = 'scientificamerican'

class SciAme(object):
    def __init__(self):
        self.__articles_url__=list()
        self.__articles_num__=0
        self.__single_soup__ = ''
        self.__article_info__ = dict()
        r=requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        As=soup.find_all('article')
        self.__articles_url__=[]
        for A in As:
            a=A.find_all('a', href=True)
            for i in a:
                if i['href'] in EXCLUDE:
                    pass
                elif "video" in  i['href']:
                    pass
                else:
                    self.__articles_url__.append(i['href'])
        self.__articles_url_ = set(self.__articles_url__)
        self.__articles_url_ = list(self.__articles_url__)
        self.__articles_num = len(self.__articles_url__)
    def get_article(self):
        url_index = random.randint(0, self.__articles_num-1)
        URL=self.__articles_url__[url_index]
        r=requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        data=soup.find_all('h1',{"class":"article-header__title t_article-title"})
        title=''
        subtitle=''
        try:
            title=data[0].text
        except:
            pass
        try:
            b=soup.find_all('p',{"class":"t_article-subtitle"})
            subtitle=b[0].text
        except:
            pass
        data=[a.find_all('p') for a in soup.find_all('div',{"class":"mura-region-local"})]
        text=[]
        for d in data:
            for i in d:
                ts=i.text.split('\xa0')
                for  t in ts:
                    text.append(t)
        self.__article_info__['title'] = title
        self.__article_info__['subtitle'] = subtitle
        self.__article_info__['text'] = text
        return self.__article_info__

#mySciAme = SciAme()
#info=mySciAme.get_article()
#print(info['title'])
#print(info['subtitle'])
#print(info['text'])

#app = Flask(__name__)
#
#@app.route('/', methods=['POST', 'GET'])
#def dict_form():
#    return render_template("dict.html", title=title,subtitle=subtitle, text=text)
#
if __name__ =="__main__":
    app.run(debug=True, port=39003, host='0.0.0.0')

