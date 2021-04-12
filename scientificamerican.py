from bs4 import BeautifulSoup
import requests
import random
import time

URL='https://www.scientificamerican.com/'
EXCLUDE=["https://www.scientificamerican.com/section/opinion/"]
headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3029.110 Safari/537.37',
    'X-Requested-With': 'XMLHttpRequest',
}

r=requests.get(URL, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
As=soup.find_all('article')
articles=[]
for A in As:
    a=A.find_all('a', href=True)
    for i in a:
        if i['href'] in EXCLUDE:
            pass
        elif "video" in  i['href']:
            pass
        else:
            articles.append(i['href'])

articles=set(articles)
articles=list(articles)
URL1=random.sample(articles, 1)[0]
print(URL1)
time.sleep(1)

#URL="https://www.scientificamerican.com/article/confirmed-we-live-in-a-simulation/"
#URL='https://www.scientificamerican.com/article/a-pep-talk-from-steven-pinker/'
#URL1='https://www.scientificamerican.com/article/in-case-you-missed-it46/'
r=requests.get(URL1, headers=headers)
if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    data=soup.find_all('h1',{"class":"article-header__title t_article-title"})
    title=data[0].text
    b=soup.find_all('p',{"class":"t_article-subtitle"})
    subtitle=b[0].text
    
    
    data=[a.find_all('p') for a in soup.find_all('div',{"class":"mura-region-local"})]
    text=[]
    for d in data:
        for i in d:
            text.append(i.text)
    
    for t in text:
        print(t)


