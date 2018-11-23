import sqlite3
con=sqlite3.connect("Database.db")
cur=con.cursor()
print 'Opened Database Successfully'
cur.execute("drop table if exists Records")
cur.execute("Create table Records (enrolment varchar2(30) PRIMARY KEY,email_id varchar2(50),username varchar2(10),password varchar2(7) ,UNIQUE(email_id))")
print 'Created Table Successfully'
con.close()