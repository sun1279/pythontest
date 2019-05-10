import json
import sys

ls=list()
with open(sys.argv[1]) as fd:
    ls=json.load(fd)

name=sys.argv[1].split('.')[0]
cnt =0
with open(name+'.csv', 'w') as fd:
    for l in ls:
        if cnt is 0:
            for key in l.keys():
                fd.write(key)
                fd.write(',')
            fd.write("\n")

        else:
            for value in l.values():
                fd.write(value)
                fd.write(',')
            fd.write("\n")
        cnt+=1
    fd.close()

                



