import math
import wave

alt=32700
def create_wav(name, sr, freq, time):
    length = (sr*time)
    fd=open(name, "wb+")
    all_list=list()
    for i in range(length):
        d=math.sin(2*(math.pi)*i/(sr/freq))
        data=round(d*alt)
        if(data < 0):
            data = ((1<<16)+data)
        d1 = (data)&0xff
        d2 = (data >> 8)&0xff
        all_list.append(d1)
        all_list.append(d2)

    pcmdata = bytearray(all_list)
    fd.write(bytearray(all_list))
    fd.close()
    with wave.open(name+".wav", 'wb') as wavfile:
        wavfile.setparams((1,2,16000,0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)

create_wav("1000hz", 16000, 1000, 10)
