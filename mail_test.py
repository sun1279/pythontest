#this case is used to test sending mail

import smtplib

#email format
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

POP_SERVER = "pop.163.com"
SMTP_SERVER = "smtp.163.com"
IMAP_SERVER = "imap.163.com"

SENDER = "@163.com"
RECEIVER = "@163.com"
PASSWD = ""

title = "[你好 我今天工作 以此邮件为准]HELLO WORLD"
content = "今天 星期一 周末 你好 谷歌浏览器 \n 南宋的开放\n"
MESSAGE = "123 HELLO WORLD 456"


#An SMTP_SSL instance behaves exactly the same as instances of SMTP. SMTP_SSL should be used for situations where SSL is required from the beginning of the connection
smtp = smtplib.SMTP_SSL(SMTP_SERVER)
#Identify yourself to an ESMTP server using EHLO
smtp.ehlo(SMTP_SERVER)
#smtp.set_debuglevel(1)
smtp.login(SENDER, PASSWD)

class SendMail(object):
    def __init__(self, mailto,subject,content,attach=[]):
        self.__mailto__ = mailto
        self.__subject__ = subject
        self.__content__ = content 
        self.__attach__ = attach

    def send(self):
        
        print("Send")
        if len(self.__attach__) == 0: #pure text
            msg=MIMEText(self.__content__, "plain", "utf-8")
            msg["Subject"] = Header(self.__subject__, "utf-8")
            msg["From"] = SENDER
            msg["To"] = self.__mailto__

        else:
            #mail with attachment
            msg = MIMEMultipart()
            msg["Subject"] = Header(self.__subject__)
            msg["From"] = SENDER
            msg["To"] = self.__mailto__
            msg.attach(MIMEText(self.__content__, "html", "utf-8"))
            
            #filenames=list()
            #filenames.append("air.sqlite")
            #filenames.append("a.out")
            #filenames.append("domain.py")
            
            #TODO file in to a list
            for filename in self.__attach__:
                att1 = MIMEText(open(filename, "rb").read(), 'base64', 'utf-8')
                att1["Content-Type"] = 'application/octet-stream'
                att1["Content-Disposition"] = 'attachment; filename='+filename
                msg.attach(att1)

        smtp.sendmail(SENDER, self.__mailto__, msg.as_string())
        smtp.quit()


filelist=['All.csv','DomesticAirCode.csv','InternationalAirCode.csv']
s=SendMail("@163.com", "[kaihui]别忘了明天一起开会", "见标题", filelist)
s.send()

