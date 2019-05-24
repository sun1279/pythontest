import tweepy
import re
import shutil
import requests
from requests_html import HTMLSession
import time

headers = {
    'Referer': 'https://twitter.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

session = HTMLSession()

CONSUMER_KEY = 'z5mK2uctiBdV4BHEWrpenqd77'
CONSUMER_SECRET = '9OcFgySBeWzApYYLmkUqg25vYFwj2pXedSnR1Sr2c7dF4Akt7d'
ACCESS_KEY = '161683541-zxsc89YPrumdIKvdB9Gyw6TvrNnN4E08zhQ1lMeT'
ACCESS_SECRET = 'curi1UsKb3KUzql6eSmiAKDyeChf3BCb4BykcIN5e967L'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


class MyTweet(object):

    def __init__(self, api):
        self.__api__ = api

        #download media file
    def download_media(self, url, filename):
        print("DDDDDDDDDDDDDDDDDDOWNLOAD")
        exit()
        try:
            r = requests.get(url, stream=True, headers=headers)
            with open(filename, 'wb') as fd:
                shutil.copyfileobj(r.raw, fd)
        except:
            print("Download error")



            
    def home(self, cnt):
        ls = list()
        try:
            ls = list(self.__api__.home_timeline(count=cnt))
        except:
            print("ERROR")
        return ls


    def user(self, user, cnt):
        ls = list()
        try:
            ls = list(self.__api__.user_timeline(user,count=cnt))
        except:
            print("ERROR")
        return ls

    def send_tweet(self, text, media=''):
        if media != '':
            self.__api__.update_with_media(media, "helloworld Nice to meet ffff")
        else:
            self.__api__.update_status(text)

    class Process(object):

        def __init__(self, l):
            self.__l__ = l
        #get full tweet text
        def get_full_text(self, url):
            try:
                r = session.get(url, headers=headers)
                newurl = r.html.text
                newurl = newurl.split('\n')[0]
                r = session.get(newurl, headers=headers)
                text = r.html.find('title')[0].text.split("\"")[1]
            except:
                print("Get Full content error")
                text=''
            return text
    

        def name(self):
            return self.__l__.author.name

        def screen_name(self):
            return self.__l__.author.screen_name

        def description(self):
            return self.__l__.author.description

        def create_at(self):
            return self.__l__.created_at

        def content(self):
            if self.__l__.truncated:  #if l.text is full content or not
                full_content_url = re.findall('https\S+', self.__l__.text)[0]
                full_content = self.get_full_text(full_content_url)
                if full_content is '': #do not get full content
                    full_content=self.__l__.text
            else:
                full_content=self.__l__.text

            return full_content
        
        def get_id(self):
            return self.__l__.id_str

        def get_media(self):
            all_files=list()
            try:
                if self.__l__.extended_entities:
                    media_lists = self.__l__.extended_entities['media']
                    for media in media_lists:
                        mediaurl = media['media_url_https']
                        all_files.append(mediaurl)
            except:
                pass
            return all_files

        def download_media(self, url_list, id_str):
            media_cnt = 0
            for url in url_list:
                postfix = url.split(".")[-1]
                download_media(url, id_str+'_'+str(media_cnt)+'.'+postfix)
            print("Download finished")

        def is_retweet(self):
            if self.__l__.is_quote_status:
                return True
            else:
                return False

        def orig_tweet(self):
            d=dict()
            if self.__l__.is_quote_status:
                try :
                    newuser=self.__l__.quoted_status
                    d['Name'] = newuser.author.name
                    d['ScreenName'] = newuser.author.screen_name
                    d['Description'] = newuser.author.description
                    d['Create'] = newuser.created_at
                    d['Content'] = newuser.text
                except:
                    print("GET ORIG ERROR")
                    pass
            return d;



t=MyTweet(api)
#t.send_tweet("Current time:2018-9-10 1234")
msg=t.home()
for m in msg:
    time.sleep(5)
    print(t.Process(m).name())
    print(t.Process(m).screen_name())
    print(t.Process(m).description())
    print(t.Process(m).create_at())
    print(t.Process(m).content())
    if t.Process(m).is_retweet():
        print(t.Process(m).orig_tweet())

