# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:05:37 2020

@author: Mynuddin
"""

# f =open('F:\IIT,BSSE\Fourth Semister\Python\Pracctice\File Handaling\First.txt','r')
# f =open(r'F:\IIT,BSSE\Fourth Semister\Python\Pracctice\File Handaling\First.txt','r')

# f = open("rainbow.txt") By Default open in read mode

f = open("Rainbow.txt","r")
print(f.read())
# print(f.read())  cursor in last dont print anythings

f.close()



#-------------------------tell()---------find cursor position-----------------

f = open("Rainbow.txt","r")
print(f"Cursor Position -> {f.tell()}")
print(f.read())
print(f"Cursor Position -> {f.tell()}")
f.close()


#-------------------------seek()---------change cursor position-----------------

f = open("Rainbow.txt","r")
print(f"Cursor Position -> {f.tell()}")
print(f.read())
print(f"Cursor Position -> {f.tell()}")
print("Before seek methods\n\n")

print("After seek methods")
f.seek(0)
print(f"Cursor Position -> {f.tell()}")

print(f.read())
f.close()




#--------------------------readline()------------single line print-------------

f = open("Rainbow.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())

f.close()




#--------------------------readlines()------------everything in a list---------

f = open("Rainbow.txt","r")
print(f.readlines())
f.close()


f = open("Rainbow.txt","r")
lines = f.readlines()
print(len(lines))

for line in lines:
    print(line,end = "")
f.close()


print(f.name)
print(f.closed)



f = open("Rainbow.txt","r")
# outputs first two characters of next line
print(f.readline(2))
f.close()



# --------------------- Read file in ---> with Block() -----------------------
# ----------------------- also called Context Manager ------------------------

with open("Rainbow.txt","r") as f:
    data = f.read()
    print(data)

print(f.closed)   # so here dont need to open or closed



with open("Rainbow.txt") as file:
    print("Name of the file:",file.name)
    print("Mode of the file:",file.mode)
    print("Mode of the file:",file.encoding)
    file.close()
print("Closed?",file.closed)


# -------------------------------- write() -----------------------------------

# if there is not any file name "File.txt" python automatically creat it
with open("File.txt","w") as file: 
    file.write("Hello Aliens")
file.close()



# now already have existing file and store some data

with open("Python.txt","w") as file: 
    file.write("Hello Aliens")
    
    # here delete the existing data  and write new data
    
file.close()

# ----------------------if i dont want it use append mode---------------------


with open("Python1.txt","a") as file: 
    
    file.write("So its my suggestion to learn python")
    
        
file.close()





# if there is no file as name python automatically creat it and append data

with open("Python2.txt","a") as file: 
    
    file.write("So its my suggestion to learn python\n")
    
        
file.close()




# -------------------------read and write , r+  ----------------------------

with open("Pythons.txt","r+") as file: 
    
    file.write("Python is just awsome") 
    print(file.read())
    
print(file.closed)

# r+   mode  not creat automatically



with open("Python3.txt","r+") as file: 
    print(file.read())
    file.write("\nPython is just awsome") 
    
print(file.closed)



# https://www.datacamp.com/community/tutorials/reading-writing-files-python



with open("mynewtextfile.txt","w+") as f:
    f.write("We are learning python\nWe are learning python\nWe are learning python")
    f.seek(0)
    print(f.read())
    print("Is readable:",f.readable())
    print("Is writeable:",f.writable())
    print("File no:",f.fileno())
    print("Is connected to tty-like device:",f.isatty())
    f.truncate(5)
    f.flush()
    f.seek(0)
    print(f.read())
f.close()

 
# copy one from to another

with open("file2.txt","r") as f:
    with open("file1.txt","w") as f1:
        f1.write(f.read())



        
# Exercise

with open("Salary.txt","r") as f:
    with open("output.txt","w") as f1:
        for line in f.readlines():          nhju
            name,salary=line.split(",")
            f1.write(f"{name}'s salary is {salary}")
          


















