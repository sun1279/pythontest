import requests
import re
import shutil 
import time


URL='http://103.230.35.222:3128'
S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https
MAX_PAGE=100

proxies1={
'http': URL,
'https': S_URL,
}

URL='http://103.230.35.222:3128'
S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https
A_URL='https://m.weibo.cn/status/'
headers = {
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#url_prefix='https://m.weibo.cn/api/container/getIndex?'
#url_prefix='https://m.weibo.cn/api/container/getIndex?value=2680925293&containerid=1076032680925293&page='
url_prefix='https://m.weibo.cn/api/container/getIndex?value=1108613250&containerid=1076031108613250&page='
page=1
url_param={
    "value":2680925293,
    "containerid":1076032680925293,
    "page":page,
}


################################################
#response=requests.get('https://m.weibo.cn/api/container/getIndex?page=1&value=5085479829&containerid=1076035085479829',proxies=proxies1, headers=headers)
#response=requests.get('https://m.weibo.cn/api/container/getIndex?value=2680925293&page=3&containerid=1076032680925293',proxies=proxies1, headers=headers)
#wb_dict=response.json()
#print(wb_dict)
###################################################
l=list()
l_pic=list()
i = 0;
j = 0;
def download_wb_image(image_url,filename):
    r=requests.get(image_url, stream=True,proxies=proxies1, headers=headers)
    with open(filename, 'wb') as fd:
        shutil.copyfileobj(r.raw, fd)

#when there is to many characters in one post,  we must expand the url the craw the FULL text
#still need to process Image/Video/Location/Retweet in this case
def get_weibo_alltext(wb_url):
    r=requests.get(wb_url, proxies=proxies1, headers=headers)
    t=r.content.decode()
    t=re.findall('\S+text".*', t)[0][9:]
    return t;


page=1
Screen_Name=''
for page in range(1, MAX_PAGE):
    i = 0



    response=requests.get(url_prefix+str(page), proxies=proxies1, headers=headers)
    print(url_prefix+str(page))
    wb_dict=response.json()
    #print(wb_dict)
    del response
    wb=wb_dict
    if 0 == wb.get('ok'):
        break
    if page == 1:
        Screen_Name=wb.get('data').get('cards')[0].get('mblog').get('user').get('screen_name')
    for l in wb.get('data').get('cards'):
        print(i)
        #print Normal Text Message
        OnlyText=''
        if wb.get('data').get('cards')[i].get('card_style'):
            print("=====================")
            i+=1
            continue
        created_at=wb.get('data').get('cards')[0].get('mblog').get('created_at')
        print(created_at)
        if '全文' in wb.get('data').get('cards')[i].get('mblog').get('text'):
            Text='123'
            #print(get_weibo_alltext(A_URL+wb.get('data').get('cards')[i].get('mblog').get('id')))
            OnlyText=Text
        else:
            Text=wb.get('data').get('cards')[i].get('mblog').get('text')
            #print(Text)
            if 'data-url' in Text:
                OnlyText=Text.split('<a data-url')[0]
                OnlyText=re.split('<.*?>', OnlyText)
                T_s=''
                for T_list in OnlyText:
                    T_s += T_list
                OnlyText = T_s
            elif 'href' in Text:
                OnlyText=re.split('<.*?>', Text)
                T_s=''
                for T_list in OnlyText:
                    T_s += T_list
                OnlyText = T_s

            elif 'span' in Text:
                OnlyText=Text.split('<')[0]
            else:
                OnlyText=Text
            if '&quot' in OnlyText:
                T_s1=''
                OnlyText=OnlyText.split('&quot;')
                for T_list in OnlyText:
                    T_s1+=T_list
                OnlyText=T_s1
        print(OnlyText)
        #Get Images if there is/are image(s)
        if wb.get('data').get('cards')[i].get('mblog').get('pics'):#picture in this post
            pic_list=wb.get('data').get('cards')[i].get('mblog').get('pics')
            for l_pic in pic_list:
                print(wb.get('data').get('cards')[i].get('mblog').get('pics')[j].get('large').get('url'))
                if i is 1:
                    pass
                    #download_wb_image(wb.get('data').get('cards')[i].get('mblog').get('pics')[j].get('large').get('url'), 'name.jpg')
                j+=1
        #still need to Process Videos
        video=wb.get('data').get('cards')[i].get('mblog').get('page_info')
        video_url=''
        if video:
            if wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info'):
                if wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info').get('mp4_sd_url'):
                    video_url=wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info').get('mp4_sd_url')
                elif wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info').get('h265_mp4_ld'):
                    video_url=wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info').get('h265_mp4_ld')
                elif wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info').get('mp4_720p_mp4'):
                    video_url=wb.get('data').get('cards')[i].get('mblog').get('page_info').get('media_info').get('mp4_720p_mp4')
    
        print(video_url)
        #and also Retweet
        retweet=wb.get('data').get('cards')[i].get('mblog').get('retweeted_status')
        if retweet:
            print(wb.get('data').get('cards')[i].get('mblog').get('retweeted_status').get('user').get('screen_name'))
            print(wb.get('data').get('cards')[i].get('mblog').get('retweeted_status').get('created_at'))        
            retweet_text=wb.get('data').get('cards')[i].get('mblog').get('retweeted_status').get('text')
            retweet_text=retweet_text.split('<')[0]
            print(retweet_text)
        #Locations
        Text=wb.get('data').get('cards')[i].get('mblog').get('text')
        #print(Text)
        if 'small_location_default' in Text:#Location
            L_str=Text.split('png')#in case there are more than one 'surl-text'
            Lo_cnt=0
            for Lo  in (L_str):
                if 'location' in Lo:
                    Lo_cnt+=1
                    break;
                else:
                    Lo_cnt+=1
            
            Location=re.findall('\S+surl-text\">(.*)\<\/span', L_str[Lo_cnt])
            #Location = re.findall('\S+surl-text\S+', Text)[0]
            ##if Location and Screen_Name not in Location:
            #Location = re.findall('surl-text">(.*)</span>', Location)
            print("Location")
            print(Location)
        i+=1
        j=0
    page+=1
    time.sleep(4)
