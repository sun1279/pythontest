URL='http://t.qq.com/sunny_21'
fullurl=URL
from requests_html import HTMLSession
session= HTMLSession()
headers = {
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
page=9
print("================================================================================")
while True:
    r = session.get(fullurl,headers=headers)
    q=r.html
    p=q.find('.noHead')[0]
    s=p.find('li')
    for i in s:
        fromId=int(i.html.split('from=')[1][1:2],10)
        myStr=i.find('.msgCnt')[0].text
        print("MY: {}".format(myStr))
        if fromId is 1:
            myTime=i.find('.pubInfo')[0].find('.time')[0].text
            print(myTime)
            try:
                picUrl=i.find('.picBox')[0].links
                print("Download pic {}".format(picUrl))
            except:
                pass
        else:
            print("-----------------------------------REPOST---------------------------------------")
            origTime=i.find('.pubInfo')[0].find('.time')[0].text
            myTime=i.find('.pubInfo')[1].find('.time')[0].text
            b=i.find('.msgCnt')[1].find('[title]')
            origUser=b[0].text
            origUser1=b[0].html.split('@')[1].split(')')[0]
    
            origStr=i.find('.replyBox')[0].text
            print('{} (@{})'.format(origUser, origUser1))
            print(origTime)
            print(origStr)
        print("================================================================================")
    
    
    #find nexzt page
    pgStr="pi="+str(page)
    urls=list(q.find('.blueFoot')[0].links)
    for url in urls:
        if pgStr in url:
            nexturl=url
            break
        else:
            nexturl=''
    
    if nexturl:
        fullurl='http://t.qq.com/sunny_21'+nexturl
    else:
        print("Finished")
        exit()
    print(fullurl)
    print("================================================================================")
    page+=1
