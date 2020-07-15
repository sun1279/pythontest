import sys
import os
l=len(sys.argv)
if l != 3:
    print("Usage: python3 hex2text input.bin output.h")
    exit()

if os.path.exists(sys.argv[1]):
    with open(sys.argv[1],'rb') as fd:
        l=len(fd.read())
        fd.seek(0)
        with open(sys.argv[2], 'w') as fd1:
            for i in range(l):
                a=fd.read(1).hex()
                b='0x'+a
                if i%16 is 0:
                    #print()
                    fd1.write('\n')
                #print(b+',',end='')
                fd1.write(b+',')
else:
    print("Error:Input file not found")
