# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 07:45:27 2020

@author: Mynuddin
"""
import tkinter as tk
from tkinter import ttk
from tkinter import  messagebox as ms_box


root_Window =tk.Tk()
root_Window.title("TAB CONTROL")
root_Window.geometry("480x480")


label_frame = ttk.LabelFrame(root_Window , text = "Contact Details")
label_frame.grid(row = 0 , column = 0 ,padx = 40 , pady = 40)


name_label = ttk.Label(label_frame , text = "Enter your name please")
age_label = ttk.Label(label_frame , text = "Enter your age please")


name_variable  = tk.StringVar()
age_variable  = tk.StringVar()

name_entry = ttk.Entry(label_frame , width = 36 , textvariable = name_variable)
age_entry = ttk.Entry(label_frame , width = 36 , textvariable = age_variable)


name_label.grid(row = 0 , column = 0 ,padx = 5 , pady = 5 ,sticky = tk.W)
age_label.grid(row = 0 , column = 1 ,padx = 5 , pady = 5,sticky = tk.W)
name_entry.grid(row = 1 , column = 0 ,padx = 5 , pady = 5,sticky = tk.W)
age_entry.grid(row = 1 , column = 1 ,padx = 5 , pady = 5,sticky = tk.W)


def func():
    ms_box.showinfo("Title" , "Content of alert box")


submit_button = ttk.Button(label_frame , text = "Submit" , command = func)
submit_button.grid(row = 2 ,columnspan = 2, padx = 40)

root_Window.mainloop()


