#python modules:---
from tkinter import *
from pymysql import *
from tkinter import messagebox
from string import ascii_letters, digits

#my modules:---
from format_check import *
from class_sql import MyDataBase
from random_string_creator import password_generator


#tkinter root-----------------------------------------------------------
root=Tk()
root.title("Sing Up Pro Version: ")
root.geometry("550x350")
root.config(bg="#FFC867")

#my variables-------
email=StringVar()
password=StringVar()
encrypt_pass=StringVar()

#my labels------------
lblEmail=Label(root, text="your email: ", bg="#FFC867")
lblEmail.config(font=("Courier", 12))
lblEmail.grid(row=3, column=2, padx=10, pady=10)

lblPass=Label(root, text="password: ", bg="#FFC867")
lblPass.config(font=("Courier", 12))
lblPass.grid(row=4, column=2, padx=10, pady=10)

#entry (intup box)---------
emailBox=Entry(root, bg="#F87C56", fg="#274017")
emailBox.config(font=("Courier", 12))
emailBox.focus()
emailBox.grid(row=3, column=3, padx=10, pady=10)

passBox=Entry(root, bg="#F87C56",show="*", fg="#274017")
passBox.config(font=("Courier", 12))
passBox.focus()
passBox.grid(row=4, column=3, padx=10, pady=10)

#my button- functions:--------------
def sing_up():
     email=emailBox.get()
     password=passBox.get()
     
     try:
          
          #MySQL CONEXION AND QUERY:
          db=MyDataBase("localhost", "root", "", "proyect")
          sql_insert="INSERT INTO user(email, password) VALUES('{}','{}')".format(email,password)
          db.insert_query(sql_insert)
          messagebox.showinfo(message="Cool! Your sign up is done!!!", title="Query message :)")
          emailBox.delete(0,END)
          passBox.delete(0,END)
          

     except TypeError:
          messagebox.showwarning(message="some kind of format error is found: please type your password again", title="Warning")
          passBox.delete(0,END)
     except OperationalError: 
           messagebox.showwarning(message="A connection cannot be established since the destination team expressly denies that connection.", title="Warning")
     except ConnectionRefusedError:
          messagebox.showwarning(message="Error connecting to the database, check your connection to the server and try again.", title="Warning")
     except InternalError:
          messagebox.showwarning(message="Check the connection data to the BD.", title="Warning")
     except IntegrityError:
          messagebox.showwarning(message="Duplicate entry email, use email for sign up or log in.", title="Warning")

#-----------------------------------------------
def passw_format():
     messagebox.showinfo(message="Between 8 and 16 characters long. Use at least 3 of the following types of characters: (a) uppercase letters, (b) lowercase letters, (c) numbers, and/or (d) special characters.", title="Password format:")
     
def random_passw():
     random_password=password_generator()
     messagebox.showinfo(message="your password is: "+random_password, title="Password format:")
     

#btns---------------
btn=Button(root, text="Sing Up", command=sing_up, bg="#FAF3E3")
btn.config(font=("Courier", 12))
btn.grid(row=5, column=2, padx=20, pady=20)

btn_passw_format=Button(root, text="Password Format", command=passw_format, bg="#FB7F64")
btn_passw_format.config(font=("Courier", 12))
btn_passw_format.grid(row=7, column=2, padx=20, pady=20)

btn_random_psw=Button(root, text="Create random password", command=random_passw, bg="#FB7F64")
btn_random_psw.config(font=("Courier", 12))
btn_random_psw.grid(row=8, column=2, padx=20, pady=20)

#close root----
root.mainloop()