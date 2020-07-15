#craw my blog using request_html
from requests_html import HTMLSession
session = HTMLSession()
headers = {
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


page_num=1
URL_PRE='https://www.cworld.info/index.php/page/'

while True:
    r = session.get(URL_PRE+str(page_num), headers=headers)
    #r = session.get('https://www.cworld.info/index.php/page/2')
    q=r.html
    ps=q.find('.post')#see html source file and find some classes,this finds all the articles
    if ps:#there is article in this page
        for p in ps:
            title=p.find('.entry-title')[0].text
            content=p.find('.entry-content')[0].text
            img = p.find('.size-large')
            print(title)
            print(content)
            if img:
                print(img[0].html.split('src=')[1].split()[0][1:-1])
            print()
    else:
        print('Exit...')
        exit()
    page_num+=1
    
