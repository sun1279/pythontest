#This case read salary sheet of some compay
#well, only my compary
info1=list()
info2=list()
info3=list()
info4=list()
info5=list()
info6=list()
info7=list()
info8=list()
info9=list()
info10=list()
info11=list()
info12=list()
info13=list()
info14=list()
info15=list()
info16=list()

cnt = 0
SECT1_SIZE = 8
SECT2_SIZE = 8
SECT3_SIZE = 5
SECT4_SIZE = 8
SECT5_SIZE = 8
SECT6_SIZE = 8
SECT7_SIZE = 7
SECT8_SIZE = 2

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


with open("ps.htm","r") as f:
    for line in f:
        lim=line.split("size=2>")
        for c in lim:
            c1=c.split("</font")
            if 'B' not in c1[0] and "HTML" not in c1[0]:
            #    print(c1[0])
                if cnt < SECT1_SIZE:
                    info1.append(c1[0])
                    #print("A".format(c1[0]))
                if cnt >=SECT1_V_OFF and cnt < SECT2_N_OFF:
                    info2.append(c1[0])
		if cnt >= SECT2_N_OFF and cnt < SECT2_V_OFF:
                    info3.append(c1[0])
	        if cnt >= SECT2_V_OFF and cnt < SECT3_N_OFF:
                    info4.append(c1[0])
		if cnt >= SECT3_N_OFF and cnt < SECT3_V_OFF:
                    info5.append(c1[0])
	        if cnt >= SECT3_V_OFF and cnt < SECT4_N_OFF:
                    info6.append(c1[0])
		if cnt >= SECT4_N_OFF and cnt < SECT4_V_OFF:
                    info7.append(c1[0])
	        if cnt >= SECT4_V_OFF and cnt < SECT5_N_OFF:
                    info8.append(c1[0])
		if cnt >= SECT5_N_OFF and cnt < SECT5_V_OFF:
                    info9.append(c1[0])
	        if cnt >= SECT5_V_OFF and cnt < SECT6_N_OFF:
                    info10.append(c1[0])
		if cnt >= SECT6_N_OFF and cnt < SECT6_V_OFF:
                    info11.append(c1[0])
	        if cnt >= SECT6_V_OFF and cnt < SECT7_N_OFF:
                    info12.append(c1[0])
		if cnt >= SECT7_N_OFF and cnt < SECT7_V_OFF:
                    info13.append(c1[0])
	        if cnt >= SECT7_V_OFF and cnt < SECT8_N_OFF:
                    info14.append(c1[0])
		if cnt >= SECT8_N_OFF and cnt < SECT8_V_OFF:
                    info15.append(c1[0])
	        if cnt >= SECT8_V_OFF and cnt < SECT9_N_OFF:
                    info16.append(c1[0])
                cnt+=1

print(cnt)
i=0
while i < SECT1_SIZE:
    print(info1.__getitem__(i)),
    print(info2.__getitem__(i))
    i+=1

i=0
while i < SECT2_SIZE:
    print(info3.__getitem__(i)),
    print(info4.__getitem__(i))
    i+=1
i=0
while i < SECT3_SIZE:
    print(info5.__getitem__(i)),
    print(info6.__getitem__(i))
    i+=1
i=0
while i < SECT4_SIZE:
    print(info7.__getitem__(i)),
    print(info8.__getitem__(i))
    i+=1
i=0
while i < SECT5_SIZE:
    print(info9.__getitem__(i)),
    print(info10.__getitem__(i))
    i+=1
i=0
while i < SECT6_SIZE:
    print(info11.__getitem__(i)),
    print(info12.__getitem__(i))
    i+=1
i=0
while i < SECT7_SIZE:
    print(info13.__getitem__(i)),
    print(info14.__getitem__(i))
    i+=1
i=0
while i < SECT8_SIZE:
    print(info15.__getitem__(i)),
    print(info16.__getitem__(i))
    i+=1
