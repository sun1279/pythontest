import poplib
from email.parser import Parser
from email.header import decode_header
import time
from str_encrypt import MyEncrypt

#POP_SERVER = "pop.gmail.com"
#SMTP_SERVER = "smtp.gmail.com"
POP_SERVER = "pop.163.com"
SMTP_SERVER = "smtp.163.com"
IMAP_SERVER = "imap.163.com"

mail_addr = "@163.com"
passwd = ""


class MailCheck(object):

    def __init__(self):
        pass

    def get_latest_mail(self, num=1):
        pop = poplib.POP3(POP_SERVER)#163
        #pop = poplib.POP3_SSL(POP_SERVER,port=995) #Gmail
        #pop.set_debuglevel(1)
        #greeting=pop.getwelcome()
        #print(greeting)
        pop.user(mail_addr)
        pop.pass_(passwd)
        cnt = 0
        #Get mailbox status. The result is a tuple of 2 integers: (message count, mailbox size).
        totalnum, totalsize=pop.stat()
        #Request message list, result is in the form (response, ['mesg_num octets', ...], octets). If which is set, it is the message to list.
        rsp, msg_list, rsp_siz = pop.list()
        ret_list=list()
        for cnt in range(num):
            rsp, msglines, msgsiz = pop.retr(totalnum-cnt)
            msg_content = b'\r\n'.join(msglines).decode('gbk')
            msg = Parser().parsestr(text=msg_content)
            ret_list.append(msg)
        return ret_list


class GetMsgInfo(object):
    
    def __init__(self, msg):
        self.__msg__ = msg
        self.__mailinfo__=dict(zip(self.__msg__.keys(), self.__msg__.values()))

    def get_sender(self):
        try:
            mail_from = self.__mailinfo__['From']
        except:
            mail_from = ''
        try:
            mail_to = self.__mailinfo__['To']
        except:
            mail_to = ''

        if "<" in mail_from:
            mail_from = mail_from.split("<")[1][:-1]
        if "<" in mail_to:
            mail_to = mail_to.split("<")[1][:-1]
        
        return (mail_from, mail_to)

    def get_subject(self):
        value = self.__msg__.get('Subject', '')
        if value.startswith("=?"):
            value,charset = decode_header(value)[0]
            subject = value.decode(charset)
        else:
            subject=value

        return subject

    def get_date(self):
        return self.__mailinfo__['Date']

    def is_attachment(self):
        if self.__msg__.is_multipart():
            for m in self.__msg__.get_payload():
                if m.get_filename():
                    return True
            return False

    def download_attach(self):
        if self.is_attachment():
            for m in self.__msg__.get_payload():
                name = m.get_filename()
                print(name)
                if name:
                    data = m.get_payload(decode=True)
                    with open(name,'wb') as fd:
                        fd.write(data)
        else:
            print("No attachment found")



    def get_content(self):
        if self.__msg__.is_multipart():
            for payload in self.__msg__.get_payload():
                type1 = payload.get_content_type()
                if type1 == 'text/html' or type1 == 'text/plain' or type1 == 'multipart/alternative':#get_content_type()
                    if len(payload.get_payload()) == 2:
                        for pay in payload.get_payload():
                            charset = pay.get_charsets()[0]
                            content = pay.get_payload(decode=True)
                    else:
                        charset = payload.get_charsets()[0]
                        content = payload.get_payload(decode=True)
        
                    content=content.decode(charset)
                #else:#type1 is 'text/base64':#attachment / or self.__msg__.get_payload()[2].get_content_disposition()
                #    name=payload.get_filename()
                #    print(name)
                #    data = payload.get_payload(decode=True)
                #    with open(name,'wb') as fd:
                #        fd.write(data)
        
        else:
            if self.__msg__.get_content_subtype() == 'html':
                content=self.__msg__.get_payload(decode=True)
            else:
                content=self.__msg__.get_payload()
        return content
        
if __name__ == '__main__':
    en = MyEncrypt()
    key1 = time.gmtime().tm_mon
    key2 = time.gmtime().tm_mday
    orig="http://www.baidu.com"
    s1 = en.encrypt(key1, orig)
    s1 = en.encrypt(key2, s1)
    
    s2 = en.decrypt(key2, s1)
    s2 = en.decrypt(key1, s2)
    print(s1)
    print(s2)
    exit()

def ProcessCmd(cmd):
    cmd_id = cmd.split()[0]
    cmd_len = len(cmd.split())
    if cmd_id == 'URL'
        url = cmd.split()[1]
        key1 = time.gmtime().tm_mon
        key2 = time.gmtime().tm_mday
        s2 = en.decrypt(key2, url)
        url = en.decrypt(key1, s2)
        #TODO  process URL
    elif cmd_id == 'TTHOME':
        cnt = 0
        if len == 2:# 3rd param defines the coun
            try:
                cnt = int(cmd.split()[1])
            except:
                cnt = 20
        else:#default 20
            cnt = 20



    elif cmd_id == 'TTUSER':
        cnt = 0
        if len == 3:# 3rd param defines the coun
            try:
                cnt = int(cmd.split()[2])
            except:
                cnt = 20
        else:#default 20
            cnt = 20
        usr = cmd.split()[1]

    elif cmd_id == 'TTSEND':#pure text
        text = cmd.split()[1]

    elif cmd_id == 'TTSEND1':#with pic
        text = cmd.split()[1]
    
mail = MailCheck()
#print(mail)
msg = mail.get_latest_mail()
for m in msg:
    c=GetMsgInfo(m)
    print(c.get_sender())
    print(c.get_date())
    print(c.get_subject())
    print(c.is_attachment())
    print(c.download_attach())
