# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:38:32 2020

@author: Mynuddin
"""


# import  tkinter
# from tkinter import*
# import  tkinter as tk

# # object = tkinter.Tk()   # Tk is the class of tkinter

# # root = tkinter.Tk() 
# root =tk.Tk()
# root.title("First Gui")
# root.mainloop() 









import  tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os 

root_Window =tk.Tk()
root_Window.title("GUI")
root_Window.geometry("480x480")

# creat labels

# ttk.Label(root_Window , text = "Enter your name :").pack()
# ttk.Label(root_Window , text = "Enter your name :").grid(row = 0 ,column =0)
# ttk.Label(root_Window , text = "Enter your age :").grid(row = 1 ,column =0)

name_label = ttk.Label(root_Window , text = "Enter your name :")
name_label.grid(row = 0 ,column =0 , sticky = tk.W)

email_label = ttk.Label(root_Window , text = "Enter your email :")
email_label.grid(row = 1 ,column =0 , sticky = tk.W)


age_label = ttk.Label(root_Window , text = "Enter your age :")
age_label.grid(row = 2 ,column =0 ,sticky = tk.W) # kepp your label in left


gender_label = ttk.Label(root_Window , text = "Gender :")
gender_label.grid(row = 3 ,column =0 ,sticky = tk.W) # kepp your label in left





# creat entry box

name_var = tk.StringVar()
name_entrybox = ttk.Entry(root_Window ,width =16 ,textvariable = name_var)
name_entrybox.grid(row = 0 , column = 1)
name_entrybox.focus()


# email entry box
email_var = tk.StringVar()
email_entrybox = ttk.Entry(root_Window ,width =16 ,textvariable = email_var)
email_entrybox.grid(row = 1 , column = 1)
 

# creat entry box
age_var = tk.StringVar()
age_entrybox = ttk.Entry(root_Window ,width =16 ,textvariable = age_var)
age_entrybox.grid(row = 2 , column = 1)
 


# creat combobox

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root_Window , width = 13 , textvariable = gender_var , state = "readonly")
gender_combobox["values"] = ("Male" , "Female" , "Others")
gender_combobox.grid(row = 3 ,column = 1)
gender_combobox.current(0)
 



# creat radio Button
usertype = tk.StringVar()
radio_button1 = ttk.Radiobutton(root_Window , text = "Student" , value = "Student" , variable = usertype)
radio_button1.grid(row = 4 ,column = 0 )


radio_button2 = ttk.Radiobutton(root_Window , text = "Teacher" , value = "Teacher" , variable = usertype)
radio_button2.grid(row = 4 ,column = 1 )
  





# Creat check button
check_var = tk.IntVar()
check_button = ttk.Checkbutton(root_Window , text = "If you want to subscribe Please check " , variable = check_var)
check_button.grid(row = 6 ,columnspan = 3)




# creat submit button

# def action():
#     user_name = name_var.get()
#     user_email = email_var.get()
#     user_age = age_var.get()
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if check_var.get() == 0:
#         subscribe = "NO"
#     else:
#         subscribe = "YES"
        
#     print(f"{user_name} --> {user_email} --> {user_age}")
#     print(f"{user_gender} --> {user_type} subscribe={subscribe}")
    
#     # This info store in a file
#     with open("file.txt","a") as file:
#         file.write(f"{user_name} \n{user_email} \n{user_age}\n{user_gender} \n{user_type} \nsubscribe={subscribe}\n")
    
#     name_entrybox.delete(0 ,tk.END)
#     age_entrybox.delete(0 ,tk.END)
#     email_entrybox.delete(0 ,tk.END)


def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if check_var.get() == 0:
        subscribe = "NO"
    else:
        subscribe = "YES"
        
    # Write to csv file
    with open("file1.csv","a") as file:
        dict_writer = DictWriter(file , fieldnames = ["User Name" , "User Email Address" , "User Gender", "User Age" , " User Type" , "Subscribe"])
        
        if os.stat("file1.csv").st_size == 0: 
            
            dict_writer.writeheader()
            
        dict_writer.writerow({
            
            "User Name" : user_name,
            "User Email Address" : user_email,
            "User Gender" : user_gender,
            "User Age"   : user_age,
            " User Type" : user_type,
            "Subscribe" : subscribe

            })
        
        
    name_entrybox.delete(0 ,tk.END)
    age_entrybox.delete(0 ,tk.END)
    email_entrybox.delete(0 ,tk.END)




submit_button = ttk.Button(root_Window , text = "Submit" , command = action )
submit_button.grid(row = 7 , column = 0)



root_Window.mainloop()
 