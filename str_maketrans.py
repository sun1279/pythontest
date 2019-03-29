s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
d='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i in d:
        cnt=d.index(i)
        cnt += 2
        if cnt > 25:
            cnt -= 26
        print(d[cnt],end='')
    else:
        print(i, end='')

print('')

d1='cdefghijklmnopqrstuvwxyzab'
table=s.maketrans(d,d1)
print(s.translate(table))
