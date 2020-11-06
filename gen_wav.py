import math



def create_wav(name, sr, freq, time):
    length = (sr*time)
    fd=open(name, "wb+")
     all_list=list()
    for i in range(length):
        d=math.sin((math.pi/180)*i*360/(sr/freq))
        data=round(d*alt)
        if(data < 0):
            data = ((1<<16)+data)
        d1 = (data)&0xff
        d2 = (data >> 8)&0xff
        all_list.append(d1)
        all_list.append(d2)

    fd.write(bytearray(all_list))
    fd.close()

create_wav("1000hz.pcm", 16000, 1000, 10)
