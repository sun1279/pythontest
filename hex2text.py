import sys
import os
l=len(sys.argv)
if ((l != 3)and(l!=4)):
    print("Usage: python3 hex2text input.bin output.h")
    exit()

if(l == 4):
    length = int(sys.argv[3])
    if (length != 1) and (length !=2) and (length !=4):
        print("ERROR")
        exit()
else:
    length = 1

if os.path.exists(sys.argv[1]):
    with open(sys.argv[1],'rb') as fd:
        l=len(fd.read())
        fd.seek(0)
        with open(sys.argv[2], 'w') as fd1:
            for j in range(l//length):
                a=fd.read(length).hex()
                b='0x'
                for i in range(length):
                    b+=(a[2*(length-i-1):2*(length-i-1)+2])
             #   print(b)
                if(j % (16/length) == 0):
                    fd1.write('\n')
                fd1.write(b+',')
            if(l%length != 0):
                a=fd.read(l%length).hex()
                b='0x'
                left_length = len(a)
                for i in range(left_length):
                    b+=(a[2*(left_length-i-1):2*(left_length-i-1)+2])
            #    print(b)
                fd1.write(b+',')
    print("Done")
                
else:
    print("Error:Input file not found")
