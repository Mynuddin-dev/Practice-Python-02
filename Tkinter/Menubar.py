# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:43:21 2020

@author: Mynuddin
"""

import tkinter as tk
from tkinter import ttk

root_Window =tk.Tk()
root_Window.title("MENUE BAR")
root_Window.geometry("480x480")

def func():
    pass


# Menue

# menuebar = tk.Menu(root_Window)

# menuebar.add_command(label = "Save" , command = func)
# menuebar.add_command(label = "Save as" , command = func)
# menuebar.add_command(label = "copy" , command = func)
# menuebar.add_command(label = "Pase" , command = func)
# menuebar.add_command(label = "Insert" , command = func)

main_manu = tk.Menu(root_Window)

file_manu = tk.Menu(main_manu ,tearoff = 0)
file_manu.add_command(label="New File", command=func)
file_manu.add_command(label="Open", command=func)
file_manu.add_command(label="Save", command=func)
file_manu.add_separator()
file_manu.add_command(label="Save All", command=func)
file_manu.add_command(label="Save As", command=func)

# Edit Menu

edit_menu = tk.Menu(main_manu , tearoff = 0)
edit_menu.add_command(label="Undo", command=func)
edit_menu.add_command(label="Redo", command=func)
edit_menu.add_command(label="Cut", command=func)
edit_menu.add_command(label="Select All", command=func)


main_manu.add_cascade(label="File" , menu =file_manu)
main_manu.add_cascade(label="Edit" , menu =edit_menu)


root_Window.config(menu = main_manu)


root_Window.mainloop()