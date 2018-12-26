import urllib.request, urllib.parse, urllib.error
import tweepy
import time
import re
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
URL='http://www.cworld.info'
CONSUMER_KEY = 'X3WVQX5OojiTF6MDE9GWWdQih'
CONSUMER_SECRET = 'EQyUQebeWAxyeOBYuSsB3OUQn8KCg1Nz8q2Wzjq8QvSfnzis7S'
ACCESS_KEY = '161683541-4h6hRODBIIc0xMXzaSKiRbyDW6lh8VOOAWNFnOvG'
ACCESS_SECRET = 'C5Q8TlkN0TxXBT9oo8g3dKwoVORiqUFDgIgaRKIWdS5XS'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#url = input('Enter - ')
URL = "http://www.cworld.info"
URL_163 = "http://sunjw.cn"
#url = "http://www.163.com"
#html = urllib.request.urlopen(url).read()
#print(html)
#links = re.findall(b'href="(http[s]?://.*?\S)"', html)
#links = re.findall(b'href="(http[s]?://.*?)"', html)
#if re.findall(b'http', html):
url_done=list()
s_url=list()
jpg_url=list()

def SUN_get_donamin_name(input_url):
    if "http" in input_url and "www" in input_url:#http://www.baidu.com
        domain_name=re.findall('\S*www.(.*)\S*',input_url)
        return domain_name[0]
    if "http" in input_url and "www" not in input_url:#http://baidu.com
        domain_name=re.findall('\/\/(.*)\S*',input_url)
        return domain_name[0]
    if "http" not in input_url and 'www' in input_url:#www.baidu.com
        domain_name=re.findall('\S*www.(.*)\S*',input_url)
        return domain_name[0]
    if "http" not in input_url and "www" not in input_url:#baidu.com
        domain_name=re.findall('\/\/(.*)\S*',input_url)
        return domain_name[0]


def SUN_find_all_the_link(url1,d_name):
    if url1.endswith("jpg") or url1.endswith("png"):
        if url1 not in jpg_url:
            jpg_url.append(url1)
        return
    if "xmlrpc" in url1:
        return
    if "wp-json" in url1:
        return
    if d_name not in url1:
        return
    if url1 not in url_done:
        url_done.append(url1)
    else:
        return
    try:
        html = urllib.request.urlopen(url1).read()
    except:
        print("error")
        return
    links = re.findall(b'href="(http[s]?://.*?\S)"', html)
    srcs = re.findall(b'src="(http[s]?://.*?\S)"', html)

    for src in srcs:#for img, this 1st
        try:
            d_link = src.decode()
            print(d_link)
        except:
           continue
        SUN_find_all_the_link(d_link,d_name)
    for link in links:#this second
        try:
            d_link = link.decode()
            print(d_link)
        except:
           continue
        if d_link in url_done:
            continue
        else:
            SUN_find_all_the_link(d_link,d_name)


SUN_find_all_the_link(URL, SUN_get_donamin_name(URL))

def SUN_download_file_jpg(jpg_url, jpg_name):
    img=urllib.request.urlopen(jpg_url).read()
    with open(jpg_name, "wb") as f:
        f.write(img)
    f.close()

def SUN_get_download_name(url):
    name=re.findall('\S*\/(.*jp\S*g)',url)
    return name[0]

l_file_name=list()
l_title=list()
l_url=list()
for a in url_done:
    if "wp-login" in a:
        continue
    if "wp-content" in a:
        continue
    if "category" in a:
        continue
    if "index.php" not in a:
        continue
    if "feed" in a:
        continue
    if "root" in a:
        continue
    if "page" in a:
        continue
    if "about-me" in a:
        continue
    #print(a)
    try:
        html=urllib.request.urlopen(a).readlines()
    except:
        print("url error")
        continue
    l_url.append(a)
    a=0
    for line in html:
        try:
            line=line.decode('utf-8')
        except:
            pass
        if "entry-title" in line:
            s=re.findall('(\[.*)<\/\S*',line)
            #print(s)
            if 'English' in s[0]:
                l_url.pop()
                continue
            l_title.append(s[0])
            continue
        else:
            if "alignnone" in line:
                s=re.findall('\S*src=\"(.*.jp\S*g)\S',line)
                l_file_name.append(SUN_get_download_name(s[0]))
                SUN_download_file_jpg(s[0],SUN_get_download_name(s[0]))

if len(l_url) == len(l_title) and len(l_title) == len(l_file_name):
    print("==================================")
cnt=0    
while cnt < len(l_url):
    txt=l_title[cnt]+'   '+l_url[cnt]
    api.update_with_media(l_file_name[cnt],status=txt)
    cnt+=1

