from Tkinter import *
from tkMessageBox import *
from xlsxwriter.workbook import Workbook
import sqlite3
con=sqlite3.connect("Database.db")
cur=con.cursor()
workbook = Workbook('Contest_Teams.xlsx')
worksheet =workbook.add_worksheet()

def reset():
	result=askyesno('Confirm','Are you sure you want to delete all the content of table?')
	if result==1:
		cur.execute("drop table if exists Records")
		cur.execute("Create table Records (enrolment varchar2(30) PRIMARY KEY,email_id varchar2(50),username varchar2(10),password varchar2(7) ,UNIQUE(email_id))")
		showinfo('Success','Table Dropped')
def gen():
	worksheet.write(0,0,'Enrolment')
	worksheet.write(0,1,'Email')
	worksheet.write(0,2,'Team Name')
	worksheet.write(0,3,'Password')
	mysel=cur.execute("select * from Records ")
	for i, row in enumerate(mysel):
	    for j, value in enumerate(row):
        	worksheet.write(i+1, j, value)
	workbook.close()
	showinfo('Success','Excel sheet \'Contest_Teams.xlsx\' has been generated.')

root=Tk()
root.geometry('260x260')
root.title('Registeration Service')
Label(root,text='Database Manager',font='Calibri 20').grid(row=0,column=0)
Button(root,text='Reset Database',command=reset).grid(row=1,column=0)
Button(root,text='Generate XLSX',command=gen).grid(row=2,column=0)
Button(root,text='Exit',command=lambda:root.destroy()).grid(row=3,column=0)

root.mainloop()
con.close()