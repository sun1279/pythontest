import requests
import shutil


URL_PREFIX="https://embed.media/api/source/"

URLO='https://www5.javqd.com/movie/caribbeancom-051119-917-jav-uncensored-the-love-affair-of-the-bride-whose-heart-is-shaking-just-before-marriage.html'

headers= {'Referer': 'https://embed.media/v/7qv7nqny2wo', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'X-Requested-With': 'XMLHttpRequest'}

ro=requests.get(URLO, headers=headers)
content=ro.content
c=content.split()

def download_wb_image(image_url,filename):
    try:
        r=requests.get(image_url, stream=True, headers=headers)
        with open(filename, 'wb') as fd:
            shutil.copyfileobj(r.raw, fd)
    except:
        print("download Image Error")

for i in c:
    for i in c:
        if "qdembed.com" in i.decode() and "https" in i.decode():
            URL1=i.decode()

    if "core.js" in i.decode():
        jsid1=i.decode()
    if "base.js" in i.decode():
        jsid2=i.decode()

URLNEW='https://www5.javqd.com/v/'

headers['Referer']=URLNEW+URL1

videoid=URL1.split('/')[-1][:-1]
print(URL_PREFIX+videoid)

r1=requests.post(URL_PREFIX+videoid, headers)
print(r1.json())

d=r1.json()
video_url1=d['data'][0]['file']
video_url2=d['data'][0]['label']
video_url3=d['data'][0]['type']
VIDEO=video_url1+'-'+video_url2+'.'+video_url3
print(VIDEO)

download_wb_image(VIDEO, videoid+'.mp4')
print('Done')

