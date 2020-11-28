import csv
from requests_html import HTMLSession
from bs4 import BeautifulSoup

my_data=dict()
#session = HTMLSession()
#URL="https://s.198704.xyz/202006.htm"
#r=session.get(URL)
#ht=r.text.encode('iso-8859-1').decode('gbk')
#soup=BeautifulSoup(ht, "lxml")
class SalaySheep():
    def __init__(self, filename):
        self.filename=filename 

    def get_info(self):
        my_data=dict()
        htmlfile = open(self.filename, 'r', encoding='gbk')
        htmlhandle = htmlfile.read()
        soup = BeautifulSoup(htmlhandle, 'lxml')
        
        all_table=soup.find_all('table')
        for table in all_table:
            all_tr=table.find_all('tr')
            len_tr = len(all_tr)
            if len_tr == 3:
                #print(all_tr[0].text)
                for i in range(1, (len_tr//2)+1):
                    all_font=all_tr[i].find_all('font')
                    all_font1=all_tr[i+(len_tr//2)].find_all('font')
                    len_font = len(all_font)
                    for j in range(len_font):
                        my_data[all_font[j].text]=all_font1[j].text
                        #print(all_font[j].text, all_font1[j].text,)
            elif len_tr > 4:
                for i in range(1, (len_tr//2), 2):
                    all_font=all_tr[i].find_all('font')
                    all_font1=all_tr[i+1].find_all('font')
                    len_font = len(all_font)
                    for j in range(len_font):
                        #print(all_font[j].text, all_font1[j].text,)
                        my_data[all_font[j].text]=all_font1[j].text
        
        
            else:
                #print(all_tr[0].text)
                pass
        return my_data


my=SalaySheep("202006.htm")
d=my.get_info()
print(d)

exit()



filename="202006.htm"
htmlfile = open(filename, 'r', encoding='gbk')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')

all_table=soup.find_all('table')
for table in all_table:
    all_tr=table.find_all('tr')
    len_tr = len(all_tr)
    if len_tr == 3:
        #print(all_tr[0].text)
        for i in range(1, (len_tr//2)+1):
            all_font=all_tr[i].find_all('font')
            all_font1=all_tr[i+(len_tr//2)].find_all('font')
            len_font = len(all_font)
            for j in range(len_font):
                my_data[all_font[j].text]=all_font1[j].text
                #print(all_font[j].text, all_font1[j].text,)
    elif len_tr > 4:
        for i in range(1, (len_tr//2), 2):
            all_font=all_tr[i].find_all('font')
            all_font1=all_tr[i+1].find_all('font')
            len_font = len(all_font)
            for j in range(len_font):
                #print(all_font[j].text, all_font1[j].text,)
                my_data[all_font[j].text]=all_font1[j].text


    else:
        #print(all_tr[0].text)
        pass

print(my_data.keys)
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames=['职工代码', '姓名', '银行账号', '个人保险账号', '个人公积金账号', '部门', '职位名称', '职衔', '职衔薪酬等级', '应发工资总计', '扣个人保险', '扣个人公积金', '扣所得税', '扣房租/水电', '独子费', '税后补项', '基薪', '职位工资', '海信龄津贴', '工资补项', '工资扣项', '加班费', '中夜班', '绩效工资基数', '个人考评等级', '公司效益系数', '应发绩效奖金', '绩效工资补项', '绩效工资扣项', '项目/课题奖', '专项奖金', '保险（单位）', '公积金（单位）', '公司支付总成本', '累计子女教育扣除', '累计赡养老人扣除', '累计继续教育扣除', '累计住房贷款利息扣除', '累计住房租金扣除']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(my_data)

#soup=BeautifulSoup(open("202006.htm"))
