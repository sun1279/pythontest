
#'''RUNNING RESULT'''
#
#Code start
#Gen created
#GEN running
#loop
#0
#loop
#2
#loop
#4
#loop
#6
#Run 2nd time
#exiting

def CreateGenerator():
    print("GEN running")
    for i in range(4):
        print("loop")
        yield i*2

print("Code start")
mygen=CreateGenerator()
print("Gen created")
for i in mygen:#CreateGenerator will not run till now
    print(i)
print("Run 2nd time")
for i in mygen:#this will not print anything
    print(i)
print("exiting")
