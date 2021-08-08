from tkinter import *
import sqlite3

root=Tk()
root.title('Database Simulation')
root.iconbitmap('C:/Users/Prafulmhrjn/OneDrive/Desktop/fences.ico')
root.geometry("400x400")

#Databases


# Create a database or connect to one
conn = sqlite3.connect('address_books.db')


#Create cursor

c = conn.cursor()
#Create table
'''
c.execute("""CREATE TABLE addresses (
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer
           )""")'''
#Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_books.db')

    # Create cursor

    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
              {
                  'first_name': first_name.get(),
                  'last_name': last_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()



    #clear the text boxes
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_books.db')

    # Create cursor

    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


#Create text boxes
first_name = Entry(root,width = 30)
first_name.grid(row=0, column=1, padx=20)
last_name = Entry(root,width = 30)
last_name.grid(row=1, column=1, padx=20)
address = Entry(root,width = 30)
address.grid(row=2, column=1, padx=20)
city = Entry(root,width = 30)
city.grid(row=3, column=1, padx=20)
state = Entry(root,width = 30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root,width = 30)
zipcode.grid(row=5, column=1, padx=20)


#Create text box labels
first_name_label = Label(root, text = "First Name")
first_name_label.grid(row=0,column=0)
last_name_label = Label(root, text = "Last Name")
last_name_label.grid(row=1,column=0)
address_label = Label(root, text = "Address")
address_label.grid(row=2,column=0)
city_label = Label(root, text = "City")
city_label.grid(row=3,column=0)
state_label = Label(root, text = "State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row=5,column=0)

#Create submit button
submit_btn = Button(root, text="Add record to database",command = submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100 )

#Create a query button
query_btn = Button(root,text="Show records",command = query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10, ipadx=137)












#Commit changes
conn.commit()
#Close connection
conn.close()

root.mainloop()