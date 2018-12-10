#weibo.py comes from http://weibo.lxyu.net/
import weibo
import time
APP_KEY=''#your owhn app key
API_SECRET=''#your own secret
URL='http://www.cworld.info'#your website or any website
c=weibo.Client(APP_KEY, API_SECRET, URL)
print(c.authorize_url)
t=input("input code: ")
c.set_code(t)
token=c.token
print(token)
