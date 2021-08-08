from tkinter import *
import sqlite3
root = Tk()

root.iconbitmap('C:/Users/Prafulmhrjn/OneDrive/Desktop/popcorn.ico')
root.title('Database Address Book')



conn = sqlite3.connect('address_book.db')

c = conn.cursor()
'''
#create table
c.execute(""" CREATE TABLE addressbook (
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer
)""")'''

def submit():
    #create a database or connect to one
    conn=sqlite3.connect('address_book.db')
    #Create cursor
    c=conn.cursor()
    #Insert into the table
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",{
        'first_name':e1.get(),
        'last_name':e2.get(),
        'address':e3.get(),
        'city':e4.get(),
        'state':e5.get(),
        'zipcode':e6.get()
    })
    print('Address inserted successfully')
    conn.commit()
    conn.close()
    #clear the text boxes
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

def query():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    #query of the database
    c.execute("Select *,old FROM addresses")

    records = c.fetchall()
    print(records)

    #Loop through the results
    print_record=''
    for record in records:
        print_record += str(record) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=9,column=0,columnspan=2)





first_name = Label(root,text = "First Name").grid(row=0,column=0)
e1 = Entry(root).grid(row=0,column=1)
last_name = Label(root,text = "Last Name").grid(row=2,column=0)
e2 = Entry(root).grid(row=2,column=1)
address = Label(root,text="Address").grid(row=3,column=0)
e3= Entry(root).grid(row=3,column=1)
city = Label(root,text="city").grid(row=4,column=0)
e4=Entry(root).grid(row=4,column=1)
state = Label(root,text="State").grid(row=5,column=0)
e5=Entry(root).grid(row=5,column=1)
zipcode = Label(root,text="zipcode").grid(row=6,column=0)
e6=Entry(root).grid(row=6,column=1)

Add_record=Button(root,text="Add record",command=submit).grid(row =8,column=1)




conn.commit()

root.mainloop()