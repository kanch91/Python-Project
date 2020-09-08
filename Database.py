import sqlite3
 
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
