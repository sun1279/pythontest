import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

try:
    cur.execute("SELECT * FROM mytest")
except:
    cur.execute("CREATE TABLE mytest (title varchar(10), num var(10))")


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
print("Write 1 finished\n")

try:
    cur.execute("SELECT * FROM mytest1")
except:
    cur.execute("CREATE TABLE mytest1 (name varchar(10), age var(10))")

cur.execute('INSERT INTO mytest1 (name, age) VALUES(?,?)',('hisense',110))
cur.execute('INSERT INTO mytest1 (name, age) VALUES(?,?)',('hisense1',123))
cur.execute('INSERT INTO mytest1 (name, age) VALUES(?,?)',('hisense2',216))
cur.execute('INSERT INTO mytest1 (name, age) VALUES(?,?)',('hisense3',12))

conn.commit()
print("Write 2 finished\n")

print("read 1 \n")
cur.execute("SELECT * FROM mytest")
for row in cur:
    print(row)
print("read 2 \n")
cur.execute("SELECT * FROM mytest1")
for row in cur:
    print(row)

print("select sunny from 1\n")
cur.execute('SELECT * FROM mytest WHERE title = "Sunny"')
for row in cur:
    print(row)
print("delete > 200 from 2\n")
cnt=200
cur.execute('DELETE FROM mytest1 WHERE age > ?', (cnt,))
cur.execute("SELECT * FROM mytest1")
for row in cur:
    print(row)
cur.execute("DELETE FROM mytest1")
conn.commit()
conn.close()
