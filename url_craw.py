import urllib.request, urllib.parse, urllib.error
import re
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://www.cworld.info"
#url = "http://www.163.com"
html = urllib.request.urlopen(url).read()
#print(html)
links = re.findall(b'href="(http[s]?://.*?\S)"', html)
#links = re.findall(b'href="(http[s]?://.*?)"', html)
#if re.findall(b'http', html):
for link in links:
    print(link.decode())
