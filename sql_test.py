import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()


cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Sunny',11))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Su',13))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Sunn',26))
cur.execute('INSERT INTO mytest (title, num) VALUES(?,?)',('Sunny',22))
conn.commit()
print("Write finished\n")
#cur.execute('SELECT title, num FROM mytest')
cur.execute('SELECT * FROM mytest WHERE title = "Sunny"')
for row in cur:
    print(row)

cur.execute('DELETE FROM mytest WHERE num < 100')
conn.commit()
conn.close()
