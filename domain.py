n=0

#numbers like 911111 or 333339 or 888888
def IsGood1(a):
    cnt = 1
    tmp = 99
    for i in range(len(a)):
        if tmp==int(a[i]):
            cnt+=1
        else:
            cnt=1
            tmp = int(a[i])

        if cnt > 4:
            return True

    return False


#numbers like 111333 
def IsGood2(a):
    cnt = 0
    tmp = 99
    for i in range(len(a)):
        if tmp==int(a[i]):
            cnt+=1
        else:
            if cnt is 3:
                cnt=1
                tmp = int(a[i])
            elif cnt is 0:
                cnt=1
                tmp = int(a[i])
            else:
                return False

    return True

#numbers like 115533 
def IsGood3(a):
    cnt = 0
    tmp = 99
    for i in range(len(a)):
        if tmp==int(a[i]):
            cnt+=1
        else:
            if cnt is 2:
                cnt=1
                tmp = int(a[i])
            elif cnt is 0:
                cnt=1
                tmp = int(a[i])
            else:
                return False

    return True

#numbers like 112233 
def IsGood4(a):
    cnt = 0
    tmp = 99
    for i in range(len(a)):
        if tmp==int(a[i]):
            cnt+=1
        else:
            if cnt is 2:
                cnt=1
                if tmp is (int(a[i])-1):
                    tmp = int(a[i])
                else:
                    return False
            elif cnt is 0:
                cnt=1
                tmp = int(a[i])
            else:
                return False

    return True

#numbers like 332211
def IsGood5(a):
    cnt = 0
    tmp = 99
    for i in range(len(a)):
        if tmp==int(a[i]):
            cnt+=1
        else:
            if cnt is 2:
                cnt=1
                if tmp is (int(a[i])-1):
                    tmp = int(a[i])
                else:
                    return False
            elif cnt is 0:
                cnt=1
                tmp = int(a[i])
            else:
                return False

    return True

#numbers like 123456
def IsGood6(a):
    cnt = 0
    tmp = 99
    for i in range(len(a)):
        if tmp is (int(a[i])-1):
            tmp=int(a[i])
            cnt+=1
        else:
            if cnt is 0:
                tmp = int(a[i])
                cnt=1
            else:
                return False

    return True



for n in range(1000000):
    a=("%06d" %(n))
    if IsGood1(a):
        print(a,end='.xyz')
        print()
    elif IsGood2(a):
        print(a,end='.xyz')
        print()
    elif IsGood4(a):
        print(a,end='.xyz')
        print()
    elif IsGood5(a):
        print(a,end='.xyz')
        print()
    elif IsGood6(a):
        print(a,end='.xyz')
        print()
    else:
        pass



