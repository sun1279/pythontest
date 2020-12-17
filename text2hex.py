import sys
import re
l=len(sys.argv)
if l != 3:
    print("Usage: python3 text2hex.py input.h output.bin")
    exit()

try:
    with open(sys.argv[1], 'r') as fd:
        l=fd.readlines()
except:
    print("Open file ({}) failed".format(sys.argv[1]))
    exit()
all_data=list()
for i in l:
    print(i)
    nums=re.findall("0x([a-z0-9]+)", i)
    print(nums)
    for num in nums:
        if(len(num) == 2):#for 0x12
            all_data.append(int(num,16))
        elif(len(num) == 4):#for 0x1234
            all_data.append(int(num[2:4],16))
            all_data.append(int(num[0:2],16))
        elif(len(num) == 8):#for 0x12345678
            all_data.append(int(num[6:8],16))
            all_data.append(int(num[4:6],16))
            all_data.append(int(num[2:4],16))
            all_data.append(int(num[0:2],16))
        else:
            #print("ERROR1 ", len(i))
            pass

print(all_data)
with open(sys.argv[2], 'wb') as fd:
    fd.write(bytearray(all_data))

