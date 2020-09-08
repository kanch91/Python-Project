from tkinter import *
import sqlite3

root = Tk()

root.geometry('600x600')

root.title("Registration Form")

Fullname = StringVar()

Email = StringVar()

var = IntVar()

c = StringVar()

var1 = StringVar()

DoB = StringVar()

Institute = StringVar()

Cityofresidence = StringVar()


def database():
    name1 = Fullname.get()

    email = Email.get()

    gender = var.get()

    country = c.get()

    prog = var1.get()

    dob = DoB.get()

    ins = Institute.get()

    cor = Cityofresidence.get()

    conn = sqlite3.connect('Form1.db')

    with conn:
        cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS StudentDetails (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT, DoB TEXT, Institute TEXT, Cityofresidence TEXT)')

    cursor.execute(
        'INSERT INTO StudentDetails (FullName,Email,Gender,country,Programming, DoB, Institute, Cityofresidence) VALUES(?,?,?,?,?,?,?,?)',
        (name1, email, gender, country, prog, dob, ins, cor))

    conn.commit()

    top = Toplevel(root)

    top.title("Acknowledgement")

    msg = Message(top, text="The details have been submitted.")

    msg.pack()

    top.mainloop()


def search1():

    root1 = Tk()

    c1 = StringVar()

    list2 = ['Name', 'Email Address', 'Gender', 'Country', 'Programming', 'DoB', 'Institute', 'City of Residence'];

    droplist = OptionMenu(root1, c1, *list2)

    droplist.config(width=15)

    c1.set('Field')

    droplist.place(x=300, y=50)

    entry_11 = Entry(root1)

    entry_11.place(x=500, y=50)

    def search():
        conn = sqlite3.connect('Form1.db')
        with conn:
            cursor = conn.cursor()
        v=c1.get()
        search=entry_11.get()
        
        timeslot = cursor.execute('''SELECT * FROM StudentDetails WHERE Fullname = ?''',(search,))
        list1 = list(cursor.fetchall())
        cursor.execute('''SELECT COUNT(*) FROM StudentDetails WHERE Fullname = ?''',(search,))
        result = cursor.fetchone()

        
        conn.commit()
        output= ';\n'.join([' '.join(row) for row in list1])
        str.replace(')','\n', END )

        if not output:
            output="No Entries found..."
        import tkinter as tk
        master = tk.Tk()
        msg = tk.Message(master, text = output)
        msg.config(font=('times', 24))
        msg.pack()
        tk.mainloop()

    Button(root1, text='Submit', width=20, bg='black', fg='white', command=search).place(x=400, y=150)





label_0 = Label(root, text="Student Details Form", width=20, font=("bold", 30))

label_0.place(x=70, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))

label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)

entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email Address", width=20, font=("bold", 10))

label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=Email)

entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))

label_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)

Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text="Country", width=20, font=("bold", 10))

label_4.place(x=70, y=280)

list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa', 'USA', 'UK', 'Australia', 'Japan'];

droplist = OptionMenu(root, c, *list1)

droplist.config(width=15)

c.set('Select Country')

droplist.place(x=240, y=280)

label_8 = Label(root, text="Languages", width=20, font=("bold", 10))

label_8.place(x=85, y=330)

var2 = IntVar()

var4 = IntVar()

var3 = IntVar()

Checkbutton(root, text="Java", variable=var1).place(x=235, y=330)

Checkbutton(root, text="C", variable=var3).place(x=350, y=330)

Checkbutton(root, text="C++", variable=var4).place(x=400, y=330)

Checkbutton(root, text="Python", variable=var2).place(x=290, y=330)

label_5 = Label(root, text="DoB", width=20, font=("bold", 10))

label_5.place(x=80, y=380)

entry_5 = Entry(root, textvar=DoB)

entry_5.place(x=240, y=380)

label_6 = Label(root, text="Institute", width=20, font=("bold", 10))

label_6.place(x=80, y=430)

entry_6 = Entry(root, textvar=Institute)

entry_6.place(x=240, y=430)

label_7 = Label(root, text="City of Residence", width=20, font=("bold", 10))

label_7.place(x=80, y=480)

entry_7 = Entry(root, textvar=Cityofresidence)

entry_7.place(x=240, y=480)

Button(root, text='Submit', width=20, bg='black', fg='white', command=database).place(x=100, y=530)

Button(root, text='Search', width=20, bg='black', fg='white', command=search1).place(x=300, y=530)

con = sqlite3.connect('Form1.db')

root.mainloop()
