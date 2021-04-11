from bs4 import BeautifulSoup
import requests

URL="https://www.newscientist.com/article/mg25033291-800-why-rescuing-the-climate-and-saving-biodiversity-go-hand-in-hand/"
URL='https://www.newscientist.com'

EXCLUDE=["https://www.scientificamerican.com/section/opinion/"]
headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

r=requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
urls=[]
data=soup.find_all('div',{"class":"section-top-content__content"})
for d in data:
    m = d.find_all('a', href=True)
    for i in m:
        if "video" not in i['href']:
            urls.append(i['href'])

data = soup.find_all('a', {"class":"card__link"})
for d in data:
    if "article" in d['href']:
        urls.append(URL+d['href'])

urls=set(urls)

data=soup.find_all('h1',{"class":"article__title"})
title=data[0].text

data=soup.find_all('p',{"class":"article__strap"})
subtitle=data[0].text

text=[]
data=soup.find_all("div",{"class":"article__content zephr-article-content"})
for d in data:
    e=d.find_all("p", {"class":None})
    for i in e:
        if "Advertisement" not in i.text:
            text.append(i.text)



for t in text:
    print(t)


