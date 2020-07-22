# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:26:20 2020

@author: Mynuddin
"""
#20 String concatenation

first_name="Md"              #snake case writings
SecondName=" Mynuddin"       #camel case writings

fn=first_name+SecondName
print(fn)
print(fn*3) 
print(fn+2) #error
print(fn+"2")
print(fn+str(3))




#21 user input
name=input("Enter your name please:")
print("Hello ",name)

#input function always take input as a string
age=input("Enter your age please:")
print("Age:"+age) #string concatenate

print(type(name))
print(type(age))


#22 int()
a=input("Enter first value:")
b=input("Enter 2nd value:")
c=a+b
print(c,type(c))


a=int(input("Enter first value:"))
b=int(input("Enter 2nd value:"))
c=a+b
print(c,type(c))



a=float(input("Enter first value:"))
b=float(input("Enter 2nd value:"))
c=a+b
print(c,type(c))



a=str(input("Enter first value:"))
b=str(input("Enter 2nd value:"))
c=a+b
print(c,type(c))



#23 one or more input in one line

a,b=(input("Enter first and 2nd value:").split())
print(a)
print(b)

a,b=(input("Enter first and 2nd value:").split(","))
print(a)
print(b)
print(type(a),type(b))




a, b = input("Enter two of your lucky number: ").split(".") 
print("First lucky number is: ", a) 
print("Second lucky number is: ", b) 


#multiple inputs in Python using input
x, y = int(input("Enter First Name: "), input("Enter Last Name: "))
print("First Name is: ", x) 
print("Second Name is: ", y)


#multiple inputs in Python using map 
x, y = map(int, input("Enter two values: ").split())
print("First Number is: ", x) 
print("Second Number is: ", y)




#multiple inputs  as a string in Python using map
#variable 1, variable 2, variable 3 = map(int,input().split())
x, y = map(str, input("Enter two values: ").split())
print("First Number is: ", x) 
print("Second Number is: ", y)



#and list comprehensive











#excercise 26
x, y , z = map(int, input("Enter two values: ").split(","))
print(f"The avg of all is :{(x+y+z)/3}")

print("The avg of all is :{}".format(int((x+y+z)/3)))

A="python"

# p [0] [-6]
# y [1] [-5]
# t [2] [-4]
# h [3] [-3]
# o [4] [-2]
# n [5] [-1]

print(A[0])
 
print(A[0] ,A[-6])
print(A[1] ,A[-5])
print(A[2] ,A[-4])
print(A[3] ,A[-3])
print(A[4] ,A[-2])
print(A[5] ,A[-1])

print(A[0:2])
print(A[:2])
print(A[2:])
print(A[-4:-2])
print(A[:])

print(A[::-1]) #reverse


print("Md Mynuddin"[0:2])
print("Md Mynuddin"[0:11:1])
print("Md Mynuddin"[0:11:2])  #start stop step
print("Md Mynuddin"[0::2])
print("Md Mynuddin"[::2])
print("Md Mynuddin"[5::-1])
print("Md Mynuddin"[::])
print("Md Mynuddin"[::-1])
print("Md Mynuddin"[-1::-1])


AB=input("Enter your name :")
print(AB[::-1])
