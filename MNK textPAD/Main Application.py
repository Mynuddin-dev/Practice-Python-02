# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:32:04 2020

@author: Mynuddin
"""

import tkinter as tk                            
from tkinter import ttk 
from tkinter import font , colorchooser ,filedialog , messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("MNK TextPAD")
main_application.wm_iconbitmap("F:/IIT,BSSE/Fourth Semister/Python/Practice with  Harshit/Tkinter/MNK textPAD/text_editor_icon.ico")


# --------------------------------- Main Menu ---------------------------------
# ================================= End Main Menu==============================
main_menu =tk.Menu()

# icons
new_icon = tk.PhotoImage(file = "icons/new.png")
open_icon = tk.PhotoImage(file = "icons/open.png")
save_icon = tk.PhotoImage(file = "icons/save.png")
save_as_icon = tk.PhotoImage(file = "icons/save_as.png")
exit_icon = tk.PhotoImage(file = "icons/exit.png")


file = tk.Menu(main_menu , tearoff = 0)

# Edit icons
copy_icon = tk.PhotoImage(file = "icons/copy.png")
paste_icon = tk.PhotoImage(file = "icons/paste.png")
cut_icon = tk.PhotoImage(file = "icons/cut.png")
clear_all_icon = tk.PhotoImage(file = "icons/clear_all.png")
find_icon = tk.PhotoImage(file = "icons/find.png")

edit = tk.Menu(main_menu , tearoff = 0)

tool_bar_icon = tk.PhotoImage(file = "icons/tool_bar.png")
Status_bar_icon = tk.PhotoImage(file = "icons/status_bar.png")

view = tk.Menu(main_menu , tearoff = 0)



# Theme icons
dark_icon = tk.PhotoImage(file = "icons/dark.png")
light_default_icon = tk.PhotoImage(file = "icons/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icons/light_plus.png")
monokai_icon = tk.PhotoImage(file = "icons/monokai.png")
night_blue_icon = tk.PhotoImage(file = "icons/night_blue.png")
red_icon = tk.PhotoImage(file = "icons/red.png")

color_theme = tk.Menu(main_menu , tearoff = 0)

# color_theme.add_command(label="Light Default",image= light_default_icon, compound = tk.LEFT)
# color_theme.add_command(label="Light Plus",image= light_plus_icon, compound = tk.LEFT)
# color_theme.add_command(label="Night Blue",image= night_blue_icon, compound = tk.LEFT)
# color_theme.add_command(label="Dark",image= dark_icon, compound = tk.LEFT)
# color_theme.add_command(label="Monokai",image= monokai_icon, compound = tk.LEFT)
# color_theme.add_command(label="Red",image= red_icon, compound = tk.LEFT)


theme_choice = tk.StringVar()
color_icon = (dark_icon  , light_default_icon , light_plus_icon , monokai_icon , red_icon , night_blue_icon)

color_dict = {
            'Dark' : ('#c4c4c4', '#2d2d2d'),
            'Light  Plus' : ('#474747', '#e0e0e0'),
            'Light Defalut' : ('#000000', '#ffffff'),
            'Red' : ('#2d2d2d', '#ffe8e8'),
            'Monokai' : ('#d3b774', '#474747'),
            'Night Blue' : ('#ededed', '#6b9dc2')
        }



# casecade
main_menu.add_cascade(label = "File" , menu = file)
main_menu.add_cascade(label = "Edit" , menu = edit)
main_menu.add_cascade(label = "View" , menu = view)
main_menu.add_cascade(label = "Color Theme" , menu = color_theme)






# --------------------------------- Tooolbar ----------------------------------

tool_bar =  ttk.Label(main_application)
tool_bar.pack(side=tk.TOP , fill = tk.X)

# fonts

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar  , width = 25 , textvariable = font_family , state = "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))  # Any index
font_box.grid(row = 0 , column=0 ,padx = 5)

# font size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar , width = 15,textvariable = size_var , state = "readonly")
font_size["values"] = tuple(range(8,101))
font_size.grid(row = 0 , column=1 ,padx = 5)
font_size.current(4)



# bold Button

bold_icon = tk.PhotoImage(file = "icons/bold.png")
bold_button = ttk.Button(tool_bar , image = bold_icon)
bold_button.grid(row = 0 , column=2  , padx =5)

# Italic Button

italic_icon = tk.PhotoImage(file = "icons/italic.png")
italic_button = ttk.Button(tool_bar , image = italic_icon)
italic_button.grid(row = 0 , column=3  , padx =5)

# Underline Button

underline_icon = tk.PhotoImage(file = "icons/underline.png")
underline_button = ttk.Button(tool_bar , image = underline_icon)
underline_button.grid(row = 0 , column=4  , padx =5)

# Font color

font_color_icon = tk.PhotoImage(file = "icons/font_color.png")
font_color_button = ttk.Button(tool_bar , image = font_color_icon)
font_color_button.grid(row = 0 , column=5 , padx =5)

# Align left

align_left_icon = tk.PhotoImage(file = "icons/align_left.png")
align_left_button = ttk.Button(tool_bar , image = align_left_icon)
align_left_button.grid(row = 0 , column=6  , padx =5)

# Align Center

align_center_icon = tk.PhotoImage(file = "icons/align_center.png")
align_center_button = ttk.Button(tool_bar , image = align_center_icon)
align_center_button.grid(row = 0 , column=7  , padx =5)

# Align right

align_right_icon = tk.PhotoImage(file = "icons/align_right.png")
align_right_button = ttk.Button(tool_bar , image = align_right_icon)
align_right_button.grid(row = 0 , column=8  , padx =5)


# ================================= End Toolbar================================




# --------------------------------- Text Editor -------------------------------

text_editor = tk.Text(main_application)
text_editor.config(wrap = "word" , relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(fill=tk.Y , side=tk.RIGHT)
text_editor.pack(fill=tk.BOTH ,expand = True)
scroll_bar.config(command = text_editor.yview)

text_editor.config(yscrollcommand = scroll_bar.set)


# font_family and font size
# Making default font & font size                                                                                       
current_font_family = "Arial"
current_font_size = 12

# def change_font(main_application): 
def change_font(event=None):# can pass event=None
    global current_font_family
    current_font_family  = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

# def change_fontsize(main_application): 
def change_fontsize(event=None):     # can pass event=None
    global current_font_size
    current_font_size  = size_var.get()
    text_editor.configure(font=(current_font_family , current_font_size))
  
    
  
font_box.bind("<<ComboboxSelected>>" , change_font)     
font_box.bind("<<ComboboxSelected>>" , change_fontsize)   


# Button Functionality
# Bold Button Functionality
# print(tk.font.Font(font = text_editor["font"]).actual()) 

def change_font_bold():
    text_bold=tk.font.Font(font=text_editor["font"])
    if text_bold.actual()["weight"]=="normal":
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    if text_bold.actual()["weight"]=="bold":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))

bold_button.configure(command=change_font_bold)


#Italic Button Functionality
def change_font_italic():
    text_italic=tk.font.Font(font=text_editor["font"])
    if text_italic.actual()["slant"]=="roman":
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    if text_italic.actual()["slant"]=="italic":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))
italic_button.configure(command=change_font_italic)



#Underline Button Functionality
def change_font_underline():
    text_underline=tk.font.Font(font=text_editor["font"])
    if text_underline.actual()["underline"]==0:
        text_editor.configure(font=(current_font_family, current_font_size, "underline"))
    if text_underline.actual()["underline"]==1:
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))
underline_button.configure(command=change_font_underline)


# Change font color functionality

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    #print(color_var) ((R,G,B),Hexacode)
    text_editor.configure(fg=color_var[1])
    
font_color_button.configure(command=change_font_color)

# Left Allignment Function
def left_align():
    text_content=text_editor.get(1.0, "end")             # Store the text
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)                      # Delete The Text
    text_editor.insert(tk.INSERT, text_content, "left")  # Than Insert the text
align_left_button.configure(command=left_align)


#Center Allignment Function

def center_align():
    text_content=text_editor.get(1.0, "end")    # Store the text
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)             # Delete The Text
    text_editor.insert(tk.INSERT, text_content, "center") #Than Insert the text
align_center_button.configure(command=center_align)

#Right Allignment Function

def right_align():
    text_content=text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")
align_right_button.configure(command=right_align)

    

#Status Bar Functionality
text_changed=False
def change_status(event=None):
    global text_changed
    if text_editor.edit_modified():  # write something?
        text_changed=True
        words=len(text_editor.get(1.0, "end-1c").split())
        characters=len(text_editor.get(1.0, "end-1c"))
        #characters=len(text_editor.get(1.0, "end-1c")).replace(" ","")
        status_bar.config(text=f"Characters: {characters} Words: {words}") 
    text_editor.edit_modified(False)
    
text_editor.bind("<<Modified>>", change_status)

text_editor.configure(font=("Arial" , 12))

# ================================= End text Editor ===========================




# ---------------------------------Main Status Bar --------------------------------

status_bar = tk.Label(main_application , text = "Status Bar")
status_bar.pack(side= tk.BOTTOM)

# ================================= End Main Status Bar =============================







# --------------------------------- Main Menu Functinality---------------------

#Main Menu Functions


#Global Variable
url= ""
#New Functionality

def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0, tk.END)


#Open Functionality

def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetype=(("Text File", "*.txt"), ("All files", "*.*")))
    try:
        with open(url, "r") as f:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, f.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


#Save Functionality

def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
            content1=text_editor.get(1.0, tk.END)
            url.write(content1)
            url.close()
    except:
        return
    
    
    
# Save As Functionality

def save_as_file(event=None):
    global url
    try:
        content=text_editor.get(1.0, tk.END)
        url=filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
        url.write(content)
        url.close()
    except:
        return
    
    
    
#Exit Functionality

def exit(event=None):
    global url
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warning", "Do You Want To Save The File?")
            if mbox is True:
                if url:
                    content=text_editor(1.0, tk.END)
                    with open(url, "w", encoding="utf-8") as f:
                        f.write(content)
                        main_application.destroy()
                else:
                    content1=str(text_editor.get(1.0, tk.END))
                    filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
                    url.write(content1)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
    
    
    
    
    
# file Command
file.add_command(label = "New" , image = new_icon , compound = tk.LEFT ,accelerator="ctrl + N" ,command = new_file)
   
file.add_command(label = "Open" , image = open_icon , compound = tk.LEFT ,accelerator="ctrl + 0" ,command=open_file)
file.add_command(label = "Save" , image = save_icon , compound = tk.LEFT ,accelerator="ctrl + S" , command=save_file)
file.add_command(label = "Save as" , image = save_as_icon , compound = tk.LEFT ,accelerator="ctrl + shift + N" , command= save_as_file)
file.add_command(label = "exit" , image = exit_icon , compound = tk.LEFT ,accelerator="ctrl + Q" , command=exit)





# Edit command

#Find Function
def find_function(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config("match", foreground="red", background="yellow")
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0, tk.END)
        new_content=content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
        
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry("450x250+500+200")
    find_dialogue.title("Find And Replace")
    find_dialogue.resizable(0,0)      # You cant resize the dialouge box
    
    find_frame=ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_frame.pack(pady=20)
    
    find_label=ttk.Label(find_frame, text="Find")
    replace_label=ttk.Label(find_frame, text="Replace")
    
    find_input=ttk.Entry(find_frame, width=30)
    replace_input=ttk.Entry(find_frame, width=30)
    
    find_button=ttk.Button(find_frame, text="Find", command=find)
    replace_button=ttk.Button(find_frame, text="Replace", command=replace)
    
    # Label grid
    find_label.grid(row=0, column=0, padx=4, pady=4)
    replace_label.grid(row=1, column=0, padx=4, pady=4)
    
    # Entry Box grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    
    # Button Grid
    find_button.grid(row=2, column=0, padx=8, pady=8)
    replace_button.grid(row=2, column=1, padx=8, pady=8)
    
    find_dialogue.mainloop()


edit.add_command(label="Copy",image= copy_icon, compound = tk.LEFT , accelerator="ctrl + c" , command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image= paste_icon, compound = tk.LEFT , accelerator="ctrl + v" , command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image= cut_icon, compound = tk.LEFT , accelerator="ctrl + x" , command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All",image= clear_all_icon, compound = tk.LEFT , accelerator="ctrl + alt + x" , command=lambda:text_editor.delete(1,tk.END))
edit.add_command(label="Find",image= find_icon, compound = tk.LEFT , accelerator="ctrl + F" , command=find_function)


# view check button

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
#View functionality

#Toolbar functionality
def toolbar_hide():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
        
#Statusbar functionality
def statusbar_hide():
    global show_statusbar 
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False 
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True


# view.add_checkbutton(label="Tool Bar" , image = tool_bar_icon ,compound = tk.LEFT)
# view.add_checkbutton(label="Status Bar" , image = Status_bar_icon ,compound = tk.LEFT)
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=toolbar_hide)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=False, variable=show_statusbar, image=Status_bar_icon, compound=tk.LEFT, command=statusbar_hide)



#Color Theme Functionality

def change_theme():
    choosen_theme=theme_choice.get()
    color_tuple=color_dict.get(choosen_theme)
    fg_color, bg_color=color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i ,image =  color_icon[count] ,variable=theme_choice , compound = tk.LEFT , command=change_theme)           
    count += 1






# ================================= End Main Menu Functinality ================


main_application.config(menu = main_menu)

#Bind ShortCut Keys Functions

main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-q>", exit)
main_application.bind("<Control-f>", find_function)


main_application.mainloop()

