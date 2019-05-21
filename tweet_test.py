import tweepy
import re
import shutil
import requests
from requests_html import HTMLSession

headers = {
    'Referer': 'https://twitter.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

session = HTMLSession()

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = '-zxsc89YPrumdIKvdB9Gyw6TvrNnN4E08zhQ1lMeT'
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#api.update_status('HELLO World')
#api.update_with_media('rtos.png', "helloworld")

ls = list(api.home_timeline(count=100))
#ls = list(api.user_timeline("nytchinese"))

#get full tweet text
def get_full_text(url):
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


#download media file
def download_media(url, filename):
    print("DDDDDDDDDDDDDDDDDDOWNLOAD")
    exit()
    try:
        r = requests.get(url, stream=True, headers=headers)
        with open(filename, 'wb') as fd:
            shutil.copyfileobj(r.raw, fd)
    except:
        print("Download error")

#with open('tt.pickle', 'rb') as fd:
#    ls=pickle.load(fd)


for l in ls:
    print("========================================================")
    print("name: {}".format(l.author.name))
    print("Screen_name: {}".format(l.author.screen_name))
    print("--------------------------------------------------------")
    print("Description: {}".format(l.author.description))
    print("--------------------------------------------------------")
    print("Created at: {}".format(l.created_at))
    if l.truncated:  #if l.text is full content or not
        full_content_url = re.findall('https\S+', l.text)[0]
        print("NEED to preocess text")
        full_content = get_full_text(full_content_url)
        if full_content is '': #do not get full content
            full_content=l.text
        print(full_content)

    else:
        print("Noooooooooooooooo NEED to preocess text")
        print(l.text)

    tweet_id = l.id_str
    #get image/video
    try:
        if l.extended_entities:
            print('Media')
            media_lists = l.extended_entities['media']
            media_cnt = 0
            for media in media_lists:
                mediatype = media['type']
                mediaurl = media['media_url_https']
                print(mediatype)
                print(mediaurl)
                postfix = mediaurl.split(".")[-1]
                download_media(mediaurl, tweet_id+str(media_cnt)+'.'+postfix)
                media_cnt += 1
    except:
        pass

    #for retweets, get original tweet info
    if l.is_quote_status:
        ids = list()
        ids.append(l.quoted_status_id_str)
        print("------------------retweet---------------------------------")
        newuser = api.statuses_lookup(ids)
        print("name: {}".format(newuser[0].author.name))
        print("Screenname: {}".format(newuser[0].author.screen_name))
        print("Desc: {}".format(newuser[0].author.description))
        print("Created: {}".format(newuser[0].created_at))
        print(newuser[0].text)
