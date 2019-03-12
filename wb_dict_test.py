#this case is used to carw my WEIBO content
#including Text/repost/images/videos/location
import requests
import re
import shutil 
import time
import json
import os


#URL='http://103.230.35.222:3128'
#S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https
URL='http://103.230.35.222:3128'
S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https
#61.178.238.122:63000

URL1='62.152.43.152:8080'
S_URL1='62.152.43.152:8080'
URL2='43.243.165.206:3128'
S_URL2='43.243.165.206:3128'
URL3='77.59.248.61:8080'
S_URL3='77.59.248.61:8080'
URL4='182.23.38.138:8080'
S_URL4='182.23.38.138:8080'
URL5='139.255.123.186:8080'
S_URL5='139.255.123.186:8080'
URL6='202.138.243.8:8080'
S_URL6='202.138.243.8:8080'
#URL7='http://122.54.20.216:8090'
#S_URL7='https://122.54.20.216:8090'
MAX_PAGE=1000

proxies1={
'http': URL,
'https': S_URL,
}
proxy_pool={
        6:{'http': URL2, 'https': S_URL2},
        5:{'http': URL1, 'https': S_URL1},
        4:{'http': URL2, 'https': S_URL2},
        3:{'http': URL3, 'https': S_URL3},
        2:{'http': URL4, 'https': S_URL4},
        1:{'http': URL5, 'https': S_URL5},
        0:{'http': URL6, 'https': S_URL6},
        }

#URL='http://103.230.35.222:3128'
#S_URL='https://103.230.35.222:3128'#must add this cause most of the website are using https
A_URL='https://m.weibo.cn/status/'
headers = {
    'Referer': 'https://m.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#url_prefix='https://m.weibo.cn/api/container/getIndex?'
url_prefix='https://m.weibo.cn/api/container/getIndex?value=2680925293&containerid=1076032680925293&page='
#url_prefix='https://m.weibo.cn/api/container/getIndex?value=1108613250&containerid=1076031108613250&page='
page=1
url_param={
    "value":2680925293,
    "containerid":1076032680925293,
    "page":page,
}

ID_FILE_NAME='WEIBO_ID.txt'
FILE_DICT_PRE='WEIBO_Page_'

l=list()
l_pic=list()
i = 0;
j = 0;
total_weibo_cnt=0

image_failed_list=dict()#save filename and url, when download image failed

def download_wb_image(image_url,filename, serv_id=1):
    try:
        r=requests.get(image_url, stream=True,proxies=proxy_pool.get(serv_id%7), headers=headers)
        with open(filename, 'wb') as fd:
            shutil.copyfileobj(r.raw, fd)
    except:
        print("download Image Error, server id:{}".format(serv_id%7))
        image_failed_list.update({filename:image_url})

#when there is to many characters in one post,  we must expand the url the craw the FULL text
#still need to process Image/Video/Location/Retweet in this case
def get_weibo_alltext(wb_url):
    r=requests.get(wb_url, proxies=proxies1, headers=headers)
    t=r.content.decode()
    t=re.findall('\S+text".*', t)[0][9:]
    return t;

#save dict to file, in case we need that later
def save_wb_to_file(wb, filename):
    with open(filename,'w') as fd:
        json.dump(wb, fd)

#get dict back from file when needed
def get_wb_from_file(filename):
    with open(filename) as fd:
        return json.load(fd)
#save text id to file 
def save_id_to_file(filename, id):
    with open(filename,'a+') as fd:
        fd.write(id)
        fd.write('\n')

#check file exists
def check_file_exists(filename):
    exists = os.path.isfile(filename)
    return exists

#before start, we should read the id list that already saved in WEIBO_ID.txt 
try:
    with open(ID_FILE_NAME) as fd:
        already_in_id_list=fd.read()
except:
    print("No id file found")
    already_in_id_list=""

need_sleep=1
page=1
Screen_Name=''
for page in range(1, MAX_PAGE):
    i = 0
    #if not downloaded  yet, download from weibo
    if check_file_exists(FILE_DICT_PRE+str(page)) is False:
        print("FILE not EXISTs")
        response=requests.get(url_prefix+str(page), proxies=proxies1, headers=headers)
        print(url_prefix+str(page))
        wb_dict=response.json()
        need_sleep = 1
        del response
    #if downloaded already, skip download from weibo server, use local file
    else:
        #print("FILE EXISTs")
        wb_dict = get_wb_from_file(FILE_DICT_PRE+str(page))
        need_sleep = 0
    #print(wb)
    wb=wb_dict
    if 0 == wb.get('ok'):
        print("URL error or Back Up Finished!!!")
        if image_failed_list:
            print("The Following images should be downloaded again")
            print(image_failed_list)
        break
    if page == 1:
        Screen_Name=wb.get('data').get('cards')[0].get('mblog').get('user').get('screen_name')
    for l in wb.get('data').get('cards'):
        print("==================================================================================")
        #print Normal Text Message
        OnlyText=''
        if wb.get('data').get('cards')[i].get('card_style'):
            print("=====================")
            i+=1
            continue
        #should check whether we've save this before
        str_id=wb.get('data').get('cards')[i].get('mblog').get('id')
        print(total_weibo_cnt, str_id)
        if str_id in already_in_id_list:
            pass #sometimes, we saved the ID, but image not saved successfully. Don't use 'continue' here
            #i+=1
            #continue
        #if not saved, save the text id this time
        else:
            pass
        created_at=wb.get('data').get('cards')[i].get('mblog').get('created_at')
        print(created_at)
        if '全文' in wb.get('data').get('cards')[i].get('mblog').get('text'):
            #Text='123'
            Text=get_weibo_alltext(A_URL+wb.get('data').get('cards')[i].get('mblog').get('id'))
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
            image_cnt=len(pic_list)
            for l_pic in pic_list:
                image_list = wb.get('data').get('cards')[i].get('mblog').get('pics')[j].get('large').get('url')
                print('DownLoading... ({} of {})'.format(j+1,image_cnt),end='')
                print(image_list)
                image_name=str_id+'_'+str(j)+'.jpg'
                if check_file_exists(image_name) is True:
                    j+=1
                    continue
                time.sleep(10)
                download_wb_image(image_list, image_name,total_weibo_cnt)
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

                print('DownLoading video.... ', end='')
                print(video_url)
                if check_file_exists(image_name) is True:
                    pass
                else:
                    download_wb_image(video_url, str_id+'.mp4')
        
        #and also Retweet
        retweet=wb.get('data').get('cards')[i].get('mblog').get('retweeted_status')
        if retweet:
            print("UserName:", end='')
            print(wb.get('data').get('cards')[i].get('mblog').get('retweeted_status').get('user').get('screen_name'))
            print("Orig Posted Date:", end='')
            print(wb.get('data').get('cards')[i].get('mblog').get('retweeted_status').get('created_at'))        
            retweet_text=wb.get('data').get('cards')[i].get('mblog').get('retweeted_status').get('text')
            #retweet_text=retweet_text.split('<')[0]
            retweet_text_list=re.split('<.*?>', retweet_text)
            retweet_text=''.join(retweet_text_list)
            print("Orig Content:", end='')
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
            print("Location")
            print(Location)
        save_id_to_file(ID_FILE_NAME, str_id)
        i+=1
        j=0
        total_weibo_cnt+=1
    #save dict last in case we were not done the first time and then download again
    save_wb_to_file(wb_dict, FILE_DICT_PRE+str(page))
    page+=1
    if need_sleep is 1:
        time.sleep(40)
    else:
        time.sleep(1)
