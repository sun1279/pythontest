#craw my blog using request_html
from requests_html import HTMLSession
session = HTMLSession()

page_num=1
URL_PRE='https://www.cworld.info/index.php/page/'

while True:
    r = session.get(URL_PRE+str(page_num))
    #r = session.get('https://www.cworld.info/index.php/page/2')
    q=r.html
    ps=q.find('.post')#see html source file and find some classes,this finds all the articles
    if ps:
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
    
