import sys
l=len(sys.argv)
if l is not 2:
    print("Filename !")
    exit()
with open(sys.argv[1],'rb') as fd:
    l=len(fd.read())
    fd.seek(0)
    for i in range(l):
        a=fd.read(1).hex()
        b='0x'+a
        if i%16 is 0:
            print()
        print(b+',',end='')
