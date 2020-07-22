# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:41:40 2020

@author: Mynuddin
"""
# def add(a,b):
#     print( a+b) 

def add(a,b):
    return a+b   # return is preferrable

A=int(input("Enter 1st value:"))
B=int(input("Enter 2nd value:"))

x=input("Enter 1st value:")
y=input("Enter 2nd value:")

print(add(x,y))

print(add(A,B))


# def p_char(name):
#     return name[-1]
# print(p_char("Mynuddin"))


# def odd_even(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "odd"
    
# print(odd_even(9))    
    
# def odd_even(num):
#     if num%2==0:
#         return "Even"
#     return "odd"
    
# print(odd_even(9))     
    

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    

# def is_even(num):
#     if num%2==0:
#         return True
#     return False
    
       

def is_even(num):
    return num%2==0
    
print(is_even(10))    
print(is_even(9))   





#Exersise 76
def cal(x,y):
    if x>y:
        print(f"{x} is greater than {y}")
    else:
        print(f"{x} is less than {y} :)")

a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))   
cal(a,b)    
    





def cal(x,y):
    if x>y:
        return x
    else:
        return y
a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))   
print("Great num is : ",cal(a,b))    
    



#Exercise 78
def calc(x,y,z):
    if x>y and x>y:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))
c=  int(input("Enter 3rd value:")) 
print("Greatest number is : ",calc(a,b,c))





def new_calc(a,b,c):
    #bigger=cal(a,b)
    return cal(cal(a,b),c)
    #return cal(bigger(a,b),c)

print("Print greates in new way:",new_calc(30,23,54))




#exercise 81
name=input("Enter a value:")
name1=name[::-1]
if name == name1:
    print("Palindrom")
else:
    print("Not Palindrom")
    
  
#using function    
def Palindrom(x):
    name1=x[::-1]
    if x == name1:
        return "Palindrom"
    else:
        return "Not Palindrom"
    
print(Palindrom(input("Enter a value:")))     
    

print(help(sum))
print(sum.__doc__)   #doc string
print(help(len))
print(len.__doc__)
        
    
    
    
    
    
    
    
    
    
    
    