#This case read salary sheet of some compay
#well, only my compary
import os
info1=list()
info2=list()



row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
row1=list()
cnt = 0
#items of each section
SECT1_SIZE = 8
SECT2_SIZE = 8
SECT3_SIZE = 5
SECT4_SIZE = 8
SECT5_SIZE = 8
SECT6_SIZE = 8
SECT7_SIZE = 7
SECT8_SIZE = 2

#offset of each section
SECT1_N_OFF=0
SECT1_V_OFF=SECT1_N_OFF+SECT1_SIZE

SECT2_N_OFF=SECT1_V_OFF+SECT1_SIZE
SECT2_V_OFF=SECT2_N_OFF+SECT2_SIZE

SECT3_N_OFF=SECT2_V_OFF+SECT2_SIZE
SECT3_V_OFF=SECT3_N_OFF+SECT3_SIZE

SECT4_N_OFF=SECT3_V_OFF+SECT3_SIZE
SECT4_V_OFF=SECT4_N_OFF+SECT4_SIZE

SECT5_N_OFF=SECT4_V_OFF+SECT4_SIZE
SECT5_V_OFF=SECT5_N_OFF+SECT5_SIZE

SECT6_N_OFF=SECT5_V_OFF+SECT5_SIZE
SECT6_V_OFF=SECT6_N_OFF+SECT6_SIZE

SECT7_N_OFF=SECT6_V_OFF+SECT6_SIZE
SECT7_V_OFF=SECT7_N_OFF+SECT7_SIZE

SECT8_N_OFF=SECT7_V_OFF+SECT7_SIZE
SECT8_V_OFF=SECT8_N_OFF+SECT8_SIZE
SECT9_N_OFF=SECT8_V_OFF+SECT8_SIZE
#SECT9_V_OFF=SECT9_N_OFF+SECT9_SIZE

def del_all_in_list(mylist):
    local_i=0
    l=len(mylist)
    while local_i < l:
        mylist.remove(0)
        local_i+=1

name_list=list()
name_pre_list=list()
pattern="htm"
for name in os.listdir("."):
    if pattern in str(name):
        name_list.append(name)

for l in name_list:
    w=l.split(".")
    name_pre_list.append(w[0])


j = 0
cnt=0
#print(name_list)
#name_list={'ps3.htm', 'ps.htm', 'ps1.htm'}
for name in name_list:
    cnt=0
    print(name)
    with open(name,"r") as f:
        for line in f:
            lim=line.split("size=2>")
            for c in lim:
                c1=c.split("</font")
#                print(c1[0])
                if '<B>' not in c1[0] and "HTML" not in c1[0]:
                    if cnt < SECT1_SIZE:
                        info1.append(c1[0])
                        #print("A".format(c1[0]))
                    if cnt >=SECT1_V_OFF and cnt < SECT2_N_OFF:
                        info2.append(c1[0])
    		    if cnt >= SECT2_N_OFF and cnt < SECT2_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT2_V_OFF and cnt < SECT3_N_OFF:
                            info2.append(c1[0])
    		    if cnt >= SECT3_N_OFF and cnt < SECT3_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT3_V_OFF and cnt < SECT4_N_OFF:
                            info2.append(c1[0])
    		    if cnt >= SECT4_N_OFF and cnt < SECT4_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT4_V_OFF and cnt < SECT5_N_OFF:
                            info2.append(c1[0])
    		    if cnt >= SECT5_N_OFF and cnt < SECT5_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT5_V_OFF and cnt < SECT6_N_OFF:
                            info2.append(c1[0])
    		    if cnt >= SECT6_N_OFF and cnt < SECT6_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT6_V_OFF and cnt < SECT7_N_OFF:
                            info2.append(c1[0])
    		    if cnt >= SECT7_N_OFF and cnt < SECT7_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT7_V_OFF and cnt < SECT8_N_OFF:
                            info2.append(c1[0])
    		    if cnt >= SECT8_N_OFF and cnt < SECT8_V_OFF:
                            info1.append(c1[0])
    	            if cnt >= SECT8_V_OFF and cnt < SECT9_N_OFF:
                            info2.append(c1[0])
                    cnt+=1
    f.close()
j+=1
#del_all_in_list(info2)

#for l1 in row1:
#    print(l1)
#print("=========")
#print(len(row1))
#print(j)
#print("=========")

i =0
j =0
n = 0
l1=54
l2=len(info2)
print(l1)
print(l2)
#while i < len(info1):
while i < l1:
    j=0
    print(info1[i]),
    while j < l2/l1:
        print(info2[j*l1+i]),
        j+=1
    print(' ')
    i+=1
i=0
with open("1.csv","r+") as f:
    while i < l1:
        j=0
        f.write(info1[i])
        f.write(',')
        while j < l2/l1:
            f.write(info2[j*l1+i]),
            f.write(',')
            j+=1
        f.write('\n')
        i+=1


