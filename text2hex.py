import sys
l=len(sys.argv)
if l is not 3:
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
        all_data.append(int(i,16))
    except:
        pass

with open(sys.argv[2], 'wb') as fd:
    fd.write(bytearray(all_data))

