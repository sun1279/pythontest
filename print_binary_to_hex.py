#read a binary file, then print the data
i = 0
with open("BF260000_256.mem","rb") as f:
    byte = 'a'
    while byte != b'':
        i+=1
        byte=f.read(4)
        print(byte.encode('hex')),
        if i%4 is 0:
            print("\n"),

f.close()
i = 0
with open("BF260000_256.mem","rb") as f:
    byte=f.read()
    for c in byte:
        i+=1
        #print(hex(ord(c))),#ord(c) str c to hex, this print 01 to 0x1 instead of 0x01
        print("0x{0:02x}".format(ord(c))),
        if i%16 is 0:
            print("\n"),
f.close()
