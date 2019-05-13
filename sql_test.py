import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

try:
    cur.execute('SELECT * FROM mytest')
except:
    cur.execute('CREATE TABLE mytest (title,num)')

cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Sunny',11))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Su',13))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Sunn',26))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Sunny',22))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('hise',52))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('hisense',222))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Hisen',112))
conn.commit()
print("Write finished\n")
#cur.execute('SELECT title, num FROM mytest')
title=('Sunny',)
cur.execute('SELECT * FROM mytest WHERE title =?', title)
#print(cur.fetchone())
print(cur.fetchall())
#for row in cur:
#    print(row)

for r in cur.execute('SELECT * FROM mytest ORDER BY num'):
    print(r)

num=222
cur.execute('DELETE FROM mytest WHERE num =?',(num,))
num=11
cur.execute('DELETE FROM mytest WHERE num =?',(num,))
cur = conn.cursor()
print("================")   
cur.execute('SELECT * FROM mytest')
for i in cur:
    print(i)
conn.commit()
conn.close()
