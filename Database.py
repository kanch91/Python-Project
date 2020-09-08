import sqlite3
import tkinter  as tk 
from tkinter import * 
 
con = sqlite3.connect('Form.db')

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM StudentDetails')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row, end="\n")
sql_fetch(con)

print(end="\n\n")

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall()) 
sql_fetch(con)

cursorObj = con.cursor()
print(cursorObj.execute('SELECT * FROM StudentDetails').rowcount)

print(end="\n\n")

win = tk.Tk()
win.geometry("815x250")
win.configure(bg='black')
win.title("Database of Student Details")

label_0 = Label(win, text="Student Details Table",bg='black', fg='white', width=20,font=("bold", 30))
label_0.place(x=200, y=70)

print(end="\n\n")

my_connect = sqlite3.connect('Form.db')
my_conn = my_connect.cursor()

my_conn.execute("SELECT * FROM StudentDetails")
i=0 
for StudentDetails in my_conn: 
    for j in range(len(StudentDetails)):
        e = Entry(win, width=10, bg='black', fg='white') 
        e.grid(row=i, column=j) 
        e.insert(END, StudentDetails[j])
    i=i+1
win.mainloop()
