#time test
import time
c_time=time.mktime(time.localtime())
c_time-=(11*60*60)#US west to Beijing Time
t1=time.localtime(c_time)
a=time.strftime("%Y年%m月%d日  %H:%M:%S", time.localtime(c_time))
print(a)
