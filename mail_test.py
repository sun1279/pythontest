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

title = "[以此邮件为准]HELLO WORLD"
content = "今天 Hi there, nice to meeto you \nAn SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters \n"
MESSAGE = "123 HELLO WORLD 456"


#An SMTP_SSL instance behaves exactly the same as instances of SMTP. SMTP_SSL should be used for situations where SSL is required from the beginning of the connection
smtp = smtplib.SMTP_SSL(SMTP_SERVER)
#Identify yourself to an ESMTP server using EHLO
smtp.ehlo(SMTP_SERVER)
smtp.set_debuglevel(1)
smtp.login(SENDER, PASSWD)


#pure Text mail content
#msg=MIMEText(content, "plain", "utf-8")
#msg["Subject"] = Header(title, "utf-8")
#msg["From"] = SENDER
#msg["To"] = RECEIVER

#mail with attachment
msg = MIMEMultipart()
msg["Subject"] = Header(title)
#msg["Subject"] = Header(title, "utf-8")
msg["From"] = SENDER
msg["To"] = RECEIVER
msg.attach(MIMEText(content, "html", "utf-8"))

filenames=list()
filenames.append("InternationalAirCode.csv")
filenames.append("DomesticAirCode.csv")
filenames.append("All.csv")

#TODO file in to a list
for filename in filenames:
    att1 = MIMEText(open(filename, "rb").read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename='+filename
    msg.attach(att1)


smtp.sendmail(SENDER, RECEIVER, msg.as_string())
smtp.quit()



