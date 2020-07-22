# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:27:13 2020

@author: Mynuddin
"""

import os

print(os.getcwd())
# os.chdir(path)  change current working directory
print(os.path)

print(os.name)
print(os.environ)

print(os.linesep)
help(os.linesep)


os.mkdir("Movies")  # creat a folder

# os.mkdir(path\FolderName)




print(os.path.exists("Movies"))

if os.path.exists("Movies"):
    print("Already Exist")
    
else:
    os.mkdir("Movies")
    
# Create a file
open("files.txt","a").close()


os.listdir()
# os.listdir(path)


# access deeply
os.chdir(r"F:\IIT,BSSE\Fourth Semister\Python")
print(os.getcwd())
os.listdir()

fileiter = os.walk(r"F:\IIT,BSSE\Fourth Semister\Python")  
# For Better Understandin you should use small patha directory

for current_path, Folder_name ,File_names in fileiter:
    print(f"Current Path : {current_path}")
    print(f"Folder Name : {Folder_name}")
    print(f"File Name : {File_names}")




# Create a file
open("files123.txt","a").close()
os.remove("files123.txt")            #delete Permanantly

os.mkdir("IIT")
os.rmdir("IIT")


# import shutil
# shutil.rmtree("filename") #file not empty 
# shutil.copy("whatfile","wherefile")
# shutil.copy("whatfile","new/wherefile")
# shutil.move("whatfile","new/wherefile")
# shutil.copytree("path copy")













