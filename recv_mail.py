import poplib
from email.parser import Parser
from email.header import decode_header

POP_SERVER = "pop.163.com"
SMTP_SERVER = "smtp.163.com"
IMAP_SERVER = "imap.163.com"

mail_addr = "@163.com"
passwd = ""

pop = poplib.POP3(POP_SERVER)
pop.set_debuglevel(1)
greeting=pop.getwelcome()
print(greeting)
pop.user(mail_addr)
pop.pass_(passwd)
#Get mailbox status. The result is a tuple of 2 integers: (message count, mailbox size).
totalnum, totalsize=pop.stat()
#Request message list, result is in the form (response, ['mesg_num octets', ...], octets). If which is set, it is the message to list.

rsp, msg_list, rsp_siz = pop.list()
rsp, msglines, msgsiz = pop.retr(totalnum-2)
msg_content = b'\r\n'.join(msglines).decode('gbk')
msg = Parser().parsestr(text=msg_content)
#print(msg)


#ONLY TEXT or with attachment
# TODO 
mailinfo=dict()
mailinfo=dict(zip(msg.keys(), msg.values()))

print("From: {}".format(mailinfo['From']))
print("To: {}".format(mailinfo['To']))

value=msg.get('Subject', '')
value,charset=decode_header(value)[0]
mailinfo['Subject']=value.decode(charset)

print("Subject: {}".format(mailinfo['Subject']))
print("Date: {}".format(mailinfo['Date']))

if msg.is_multipart():
    for payload in msg.get_payload():
        #type1, _ = payload.get_params()[0]
        type1 = payload.get_content_type()
        if type1 == 'text/html' or type1 == 'text/plain' or type1 == 'multipart/alternative':#get_content_type()
            if len(payload.get_payload()) == 2:
                charset = payload.get_payload()[0].get_charsets()[0]
                content = payload.get_payload()[0].get_payload(decode=True)
            else:
                print(len(payload.get_payload()[0]))
                charset = payload.get_charsets()[0]
                content = payload.get_payload(decode=True)

            content=content.decode(charset)
            print("Content:======================\n{}".format(content))
            print("==============================")
        else:#type1 is 'text/base64':#attachment / or msg.get_payload()[2].get_content_disposition()
            name=payload.get_filename()
            print(name)
            data = payload.get_payload(decode=True)
            with open(name,'wb') as fd:
                fd.write(data)



