import sqlite3
con=sqlite3.connect('Mydb')
cur=con.cursor()
#cur.execute('drop table usermail')
#optimise
cur.execute('create table if not exists usermail(username varchar2(20),email varchar2(50) PRIMARY KEY)')
cur.execute('select * from usermail')

print cur.fetchall()