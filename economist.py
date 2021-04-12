from bs4 import BeautifulSoup
import requests
import random
import time
URL="https://www.economist.com/business/2021/04/08/chinas-rulers-want-more-control-of-big-tech"

EXCLUDE=["https://www.scientificamerican.com/section/opinion/"]
headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

URL='https://www.economist.com'
r=requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
data=soup.find_all('a',{"class":"headline-link"})
urls=[]
for d in data:
    urls.append(URL+d['href'])

for url in urls:
    print(url)

URL1=random.sample(urls, 1)[0]

time.sleep(2)
r=requests.get(URL1, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

data=soup.find_all('span',{"class":"article__headline"})
title=data[0].text

data=soup.find_all('span',{"class":"article__subheadline"})
subtitle=data[0].text

data=soup.find_all('p',{"class":"article__body-text"})
text=[]
for d in data:
    text.append(d.text)

print(text)

