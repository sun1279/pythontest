#print all the links inside the given website
#there is no delay between each url request,so this cannot be used in some website
import urllib.request, urllib.parse, urllib.error
import re
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
URL = "http://www.sunjw.cn"
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

request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/58.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://cworld.info",#where to come
        "Connection": "keep-alive" 
        }


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
        request = urllib.request.Request(URL,headers=request_headers)
        html = urllib.request.urlopen(request).read()
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


SUN_find_all_the_link(URL_163, SUN_get_donamin_name(URL_163))

def SUN_download_file_jpg(jpg_url, jpg_name):
    img=urllib.request.urlopen(jpg_url).read()
    with open(jpg_name, "wb") as f:
        f.write(img)
    f.close()

def SUN_get_download_name(url):
    name=re.findall('\S*\/(.*jp\S*g)',url)
    return name[0]

exit()
