import sys
l=len(sys.argv)
if l != 3:
    print("Usage: python3 text2hex.py input.h output.bin")
    exit()

try:
    with open(sys.argv[1], 'r') as fd:
        l=fd.read()
except:
    print("Open file ({}) failed".format(sys.argv[1]))
    exit()
all_data=list()
for i in l.split(','):
    try:
        i=i.strip()
        if i.startswith("0x"):
            if(len(i) == 4):#for 0x12
                all_data.append(int(i,16))
            elif(len(i) == 6):#for 0x1234
                all_data.append(int(i[4:6],16))
                all_data.append(int(i[0:4],16))
            elif(len(i) == 10):#for 0x12345678
                all_data.append(int(i[8:10],16))
                all_data.append(int(i[6:8],16))
                all_data.append(int(i[4:6],16))
                all_data.append(int(i[0:4],16))
            else:
                #print("ERROR1 ", len(i))
                pass
    except:
        print("ERROR?")
        pass

with open(sys.argv[2], 'wb') as fd:
    fd.write(bytearray(all_data))

