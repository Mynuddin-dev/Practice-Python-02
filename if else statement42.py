# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:23:33 2020

@author: Mynuddin
"""
#https://www.geeksforgeeks.org/python-if-else/?ref=lbp


# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")






num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
    
    
    
    
num = 3.4
# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
    
    
i = 20; 
if (i < 15): 
    print ("i is smaller than 15") 
    print ("i'm in if Block") 
else: 
    print ("i is greater than 15") 
    print ("i'm in else Block") 
print ("i'm not in if and not in else Block") 
    
    
    
    
    
#This time we use nested if statement

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")    
    
    
    
    
i = 10
if (i == 10): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 15")     
    
    
    
    
# Python program to illustrate if-elif-else ladder   
i = 20
if (i == 10): 
    print ("i is 10") 
elif (i == 15): 
    print ("i is 15") 
elif (i == 20): 
    print ("i is 20") 
else: 
    print ("i is not present")    
    
    
    
name=input("Enter your name:")
age=int(input("Enter your age:"))   

if name.startswith("M") or name.startswith("m") and age > 18:
    if "y" in name:                         #in keyword
        print("y is present in the name")
    else:
        print("y is not present in the name")
        
    print("User can watch the TV series ")
    
else:
    print("User can't watch this tv series")
    



#check empty or not

if name:
    print("String is not empty")
else:
    print("String is empty")
    

    
if len(name)>0:
    print("String is not empty")
else:
    print("String is empty")
    
    
    
    
k=""      
if not k:
    print("String is empty")
else:
    print("String is not empty")    
    
  
    
  
    
    
# to check if string is empty 
# using not + strip() 
  
# inilializing string 
test_str1 = "" 
test_str2 = "  "
  
# checking if string is empty 
print ("The zero length string without spaces is empty ? : ", end = "") 
if(not (test_str1 and test_str1.strip())): 
    print ("Yes") 
else : 
    print ("No") 
  
# prints Yes 
print ("The zero length string with just spaces is empty ? : ", end = "") 
if(not(test_str2 and test_str2.strip())): 
    print ("Yes") 
else : 
    print ("No")     
    
    
    
    
    

# using not + isspace() 
# inilializing string 
test_str1 = "" 
test_str2 = "  "
# checking if string is empty 
print ("The zero length string without spaces is empty ? : ", end = "") 
if(not (test_str1 and not test_str1.isspace())): 
    print ("Yes") 
else : 
    print ("No") 
  
# prints Yes  
print ("The zero length string with just spaces is empty ? : ", end = "") 
if(not (test_str2 and not test_str2.isspace())): 
    print ("Yes") 
else : 
    print ("No")     
    
    
    
 
           #Chaining comparison operators in Python
#https://www.geeksforgeeks.org/chaining-comparison-operators-python/?ref=lbp
#List of comparison operators in Python:
    
#">" | "<" | "==" | ">=" | "<=" | "!=" | "is" ["not"] | ["not"] "in"

# Python code to illustrate 
# chaining comparison operators 
x = 5
print(1 < x < 10) 
print(10 < x < 20 ) 
print(x < 10 < x*10 < 100) 
print(10 > x <= 9) 
print(5 == x > 4)  
    
    
 
# Python code to illustrate 
# chaining comparison operators 
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e is f 
exp2 = a is d > f is not c 
print(exp1) 
print(exp2) 
    