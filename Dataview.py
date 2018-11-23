import sqlite3
con=sqlite3.connect("Database.db")
cur=con.cursor()
print 'Opened Database Successfully'
cur.execute("select * from Records")
x=cur.fetchall()
print x
con.close()
