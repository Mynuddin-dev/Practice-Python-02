# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:25:52 2020

@author: Mynuddin
"""

import tkinter as tk
from tkinter import ttk

root_Window =tk.Tk()
root_Window.title("Label Frame")
root_Window.geometry("480x480")

label_frame = ttk.Labelframe(root_Window , text = "Enter your details Please :")
label_frame.grid(row = 0 ,column = 0 ,padx = 20 ,pady =10)


labels = ["What is your name : " , "Age : " , "Email :"
          ,"Gender :" , "Nationality : ","City :"]

for i in range(len(labels)):
    current_label = "Label" + str(i)
    current_label = ttk.Label(label_frame ,text = labels[i])
    current_label.grid(row = i ,column = 0 , sticky = tk.W , padx =30 ,pady = 10)





# # # creat entry box
name_var = tk.StringVar()

user_info ={
    
    "Name" :tk.StringVar(),
    "Age"  :tk.StringVar(),
    "Email":tk.StringVar(),
    "Gender":tk.StringVar(),
    "Nationality":tk.StringVar(),
    "City" : tk.StringVar()
}


counter = 0
for i in user_info:
    current_entry = "Entry_" + i  # Entry_Name - Entry_Age
    current_entry= ttk.Entry(label_frame ,width =16 ,textvariable = user_info[i])
    current_entry.grid(row = counter ,column = 1 ,padx = 20 , pady = 10)
    # Here dont need to padding(use label padding) but recomended
    counter += 1


def Submit():
    print(user_info["Name"].get())
    print(user_info["Age"].get())
    print(user_info["Email"].get())
    print(user_info["Gender"].get())
    print(user_info["Nationality"].get())
    print(user_info["City"].get())


submit_button = ttk.Button(label_frame , text = "Submit" , command = Submit )
submit_button.grid(row = 7 , columnspan =2 ,pady =10)  

for child in label_frame.winfo_children(): #return a list of all widegts
    child.grid(padx = 4 , pady = 4)



root_Window.mainloop()