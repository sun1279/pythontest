import math
import sys
total=0
cnt = 0
if len(sys.argv) != 2:
    print("param must be 2")
    exit(0)

with open(sys.argv[1], 'rb') as fd:
    cnt = fd.seek(0,2)
    cnt = cnt//2
    fd.seek(0,0)
    for i in range(cnt):
        num = fd.read(2)
        num=int.from_bytes(num, byteorder="little", signed="True")
        total += (num*num)

dbfs=20*math.log10(math.sqrt(total/cnt)/32768)+3.013
print("%.2f"% dbfs);
