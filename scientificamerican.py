from bs4 import BeautifulSoup
import requests

URL='https://www.scientificamerican.com/'
headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#r=requests.get(URL, headers=headers)
#
#soup = BeautifulSoup(r.content, 'html.parser')
#As=soup.find_all('article')
#for A in As:
#    a=A.find_all('a', href=True)
#    for i in a:
#        print(i['href'])

URL="https://www.scientificamerican.com/article/confirmed-we-live-in-a-simulation/"
r=requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
data=soup.find_all('h1',{"class":"article-header__title t_article-title"})
print(data[0].text)
b=soup.find_all('p',{"class":"t_article-subtitle"})
print(b[0].text)


data=[a.find_all('p') for a in soup.find_all('div',{"class":"mura-region-local"})]
text=[]
for d in data:
    for i in d:
        text.append(i.text)

for t in text:
    print(t)


