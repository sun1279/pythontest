#This case gets ip list from /var/log/ufw.log 
#write only ip address to ip.txt
import re
import sys
linecnt=0
f = open("ufw.log", "r")
fnew = open("ip.txt", "r+")
for line in f:
    line=line.strip()
    x =  re.findall('\s*SRC=([0-9.]+)+', line)
#    print(x)
    for item in x:
#	print(item)
        fnew.write(item)
    fnew.write("\n")

f.close()
fnew.close()
