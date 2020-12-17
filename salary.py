import csv
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os

fieldnames= ['年月','职衔','职衔薪酬等级','薪酬等级','姓名',  '职工代码', '部门', '实发金额', '基薪', '实发工资总计',  '薪酬等级','累计住房贷款利息扣除', '年度绩效基数', '海信龄津贴', '年终奖所得税', '累计赡养老人扣除', '薪酬等级', '考评等级', '烤火费', '独子费', '工资扣项', '职衔工资', '应发年终奖', '补发奖金', '年终奖基数', '专业线得分', '项目/课题奖', '职位工资', '所得税', '保险（个人）', '个人考评等级', '绩效工资合计', '职位名称', '职衔薪酬等级', '高温费', '年终奖', '其他补贴', '专项考核', '绩效工资兑现系数', '应发绩效工资', '累计支付成本', '职衔', '扣发年终奖', '绩效补项', '保险（单位）', '备注', '扣房租/水电', '累计住房租金扣除', '实发工资总计', '应发优秀绩效奖金', '应发年度绩效工资', '个人考核得分', '专项奖金', '实发基薪', '奖金合计', '累计子女教育扣除', '扣个人公积金', '部门考核得分', '税后扣项', '高温（烤火）补贴', '工资补项', '考核得分', '应出勤天数', '累计继续教育扣除', '绩效工资税额', '2月应发放金额', '扣个人保险', '奖金基数', '税额', '公司效益系数', '项目系数', 'E-MAIL', '扣发奖金', '绩效扣项', '扣公房', '业绩工资税额', '保密津贴', '公积金（单位）', '工资补贴', '绩效工资基数', '公积金（个人）', '身份证号', '个人保险帐号', '绩效工资补项', '加班费', '年度公司效益系数', '年终奖实发', '个人公积金账号',  '年终奖合计', '银行账号', '专业线排序', '培训费', '职位津贴', '个人考评', '应发绩效奖金', '个人公积金帐号', '产量完成率', '银行帐号', '应发奖金', '应发工资总计', '福利合计', '部门', '保健费', '交通补贴', '中夜班', '个人保险账号', '专业线系数', '税后补项', '特殊激励', '应发业绩', '扣所得税', '年月', '其他激励', '项目绩效', '公司支付总成本', '绩效工资扣项', '扣自房', '专项扣除累计总额', '年终考核得分', '项目线得分', '项目得分', '扣款', '住房补贴', '']
my_list=list()
my_data=dict()
#session = HTMLSession()
#URL="https://s.198704.xyz/202006.htm"
#r=session.get(URL)
#ht=r.text.encode('iso-8859-1').decode('gbk')
#soup=BeautifulSoup(ht, "lxml")
class SalaySheep():
    def __init__(self, filename):
        self.filename=filename 

##################################
# <table>
#   <tr>
#   <tr>
#       <font>
#       <font>
#       <font>
#   <tr>
#       <font>
# <table>
#################################
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


#my=SalaySheep("201703.htm")
#d=my.get_info()
#print(d)

#all_html = os.listdir("html/")
#for html_file in all_html:
#    print(html_file)
#    my=SalaySheep("./html/"+html_file)
#    d=my.get_info()
#    for i in d.keys():
#        my_list.append(i)
#    print(d)

#my_list=(set(my_list))
#my_list=(list(my_list))

with open('names.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    all_html = os.listdir("html/")
    for html_file in all_html:
        print(html_file)
        my=SalaySheep("./html/"+html_file)
        d=my.get_info()
        writer.writerow(d)


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

