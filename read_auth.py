#get ip list from /var/log/auth.log
# use key word from cause each connection starts being recorded using a "From" word
import re
l=list()
mystr="from"
f = open("auth.log")
f_ip = open("ip.txt", "r+")
for line in f:
    line=line.strip()
    if mystr in line:
        x=re.findall('from\S* [0-9.]+', line) # read line, find the word "from", then a space, then [0-9] till next blank
	#x=re.findall('\S* [0-9.]+',line)
	l.append(x)
#	print(type(x))
        #print(x[1])
    
for a in l:
    print(str(a)[7:-2])
    f_ip.write((str(a)[7:-2]))
    f_ip.write("\n")
    
f.close()
f_ip.close()
