# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:32:12 2020

@author: Mynuddin
"""

name= "Md Mynuddin"
age=22
print("Hello ",name,"your age is",age)
print("Hello "+name+" your age is "+str(age)) #just concate

#online interpreter thats work
print("Hello {} your age is {}".format(name,age))  #python 3 

#now python 3.6
print(f"Hello {name} your age is {age+2}")   #never forget f





#https://www.geeksforgeeks.org/python-format-function/
# position matters

# value stored in a variable 
str = "This article is written in {}"
print (str.format("Python")) 
  
# formatting a string using a numeric constant 
print ("Hello, I am {} years old !".format(18))  


# Number of placeholders are four but 
# there are only three values passed 
# parameters in format function. 
my_string = "{}, is a {} {} science portal for {}"
  
print (my_string.format("GeeksforGeeks", "computer", "geeks")) 
print (my_string.format("GeeksforGeeks", "computer", "geeks","Anyone")) 




# different datatypes can be used in formatting 
print ("Hi ! My name is {} and I am {} years old".format("Mynuddin", 19)) 
  
# The values passed as parameters 
# are replaced in order of their entry 
print ("This is {} {} {} {}".format("one", "two", "three", "four")) 



# Positional arguments 
# are placed in order 
print("{0} love {1}!!".format("GeeksforGeeks","Geeks")) 
  
# Reverse the index numbers with the 
# parameters of the placeholders 
print("{1} love {0}!!".format("GeeksforGeeks", "Geeks")) 
  
  
print("Every {} should know the use of {} {} programming and {}"
    .format("programmer", "Open", "Source", "Operating Systems")) 
  
  
# Use the index numbers of the 
# values to change the order that 
# they appear in the string 
print("Every {3} should know the use of {2} {1} programming and {0}"
        .format("programmer", "Open", "Source", "Operating Systems")) 
  
  
# Keyword arguments are called 
# by their keyword name 
print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg ="GeeksforGeeks")) 




# Convert base-10 decimal integers  
# to floating point numeric constants 
print ("This site is {0:f}% securely {1}!!". 
                    format(100, "encrypted")) 
  
# To limit the precision 
print ("My average of this {0} was {1:.2f}%"
            .format("semester", 78.234876)) 
  
# For no decimal places 
print ("My average of this {0} was {1:.0f}%"
            .format("semester", 78.234876)) 
  
# Convert an integer to its binary or 
# with other different converted bases. 
print("The {0} of 100 is {1:b}"
        .format("binary", 100)) 
          
print("The {0} of 100 is {1:o}"
        .format("octal", 100)) 





# To demonstrate spacing when  
# strings are passed as parameters 
print("{0:4}, is the computer science portal for {1:8}!"
                        .format("GeeksforGeeks", "geeks")) 
  
# To demonstrate spacing when numeric 
# constants are passed as parameters. 
print("It is {0:5} degrees outside !".format(40)) 
  
# To demonstrate both string and numeric 
# constants passed as parameters 
print("{0:4} was founded in {1:16}!"
    .format("GeeksforGeeks", 2009)) 
  
  
# To demonstrate aligning of spaces 
print("{0:^16} was founded in {1:<4}!"
        .format("GeeksforGeeks", 2009)) 
  
print("{:*^20s}".format("Geeks"))  # dont understand this




#Application for organize data

# which prints out i, i ^ 2, i ^ 3, 
#  i ^ 4 in the given range 
  
# Function prints out values 
# in an unorganized manner 
def unorganized(a, b): 
    for i in range (a, b): 
        print ( i, i**2, i**3, i**4 ) 
  
# Function prints the organized set of values 
def organized(a, b): 
    for i in range (a, b): 
  
        # Using formatters to give 6  
        # spaces to each set of values 
        print("{:6d} {:6d} {:6d} {:6d}"
        .format(i, i ** 2, i ** 3, i ** 4)) 
  
# Driver Code 
n1 = int(input("Enter lower range :-\n")) 
n2 = int(input("Enter upper range :-\n")) 
  
print("------Before Using Formatters-------") 
  
# Calling function without formatters 
unorganized(n1, n2) 
   
print() 
print("-------After Using Formatters---------") 
print() 
  
# Calling function that contain 
# formatters to organize the data 
organized(n1, n2)








#method
name="Md MyNuDdIn"
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("I"))
print(name.count("d"))
print(name.startswith("M"))
print(name.startswith("M"))
print(name.endswith("n"))
print(name.startswith("k"))


s="          Mynuddin           "
s2="         Mynu     ddin           "
d="..........."
print(s+d)
print(s.lstrip()+d)
print(s.rstrip()+d)
print(s.strip()+d)

print(s2)
print(s2+d)
print(s2.replace(" ",""))
print(s2.replace(" ","")+d)

s3="is She is beautiful and ugly bacause times matters is"
print(s3.replace(" ","_"))
print(s3.replace("s","SS"))
print(s3.replace(" ","_",2))

print(s3.find("is"))
print(s3.find("S"))
print(len(s3))
print(s3.find("is", 0))
print(s3.find("is", 3))
print(s3.find("is", 8))

s4="Ragnar" #6
print(s4.center(10,"#"))
print(s4.center(12,"*"))
print(s4.center(10,"#"))

s5=input("Enter name :")
print(s5.center(len(s5)+5,"$"))
#print(s5.center(len(s5)+2,"fuck"))  #The fill character must be exactly one character long




n,char=input("Enter name and character").split(",")
print(f"length of n: {len(n)} and \nnum of character:{n.lower().count(char.lower())}")
print(f"length of n: {len(n)} and \nnum of character:{n.strip().lower().count(char.strip().lower())}")





