# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:56:22 2020

@author: Mynuddin
"""



numbers=[1,2,3]   #list Set Tuple Dictionary Iterable
print(numbers)
print(square)

for i in numbers:
    print(i)
    
num=iter(numbers) #the iter call will return an iterator objec 

print(next(num))
print(next(num))
print(next(num))
print(next(num))
# i can call next cunt only iterator

print(next(numbers)) # because its not iterators

square= map(lambda i:i*2 ,numbers)#Iterator > map func  dont need apply iter()
 
# map() already iterator







# ------------------------------generators-------------------------------------

# Generators are iterator
# why use generators not list ?
# Generators provide a ""space efficient method""
# at a time work with one
# Generator provides a quick way (We don’t need to write __next__ and __iter__ methods here). 


# memory =[-------------------store in the memory-------------List-----------]
# here time , space 

 
# memory =[at a time generate one ] 
# --> (1) than (2) delet before item than (3) delet before item not(whole list)


# When you want to use a sequence again and again -----> use list
# But when you want to use a sequence one time --> Generators Best 


# creat your first Generators 
# 1:) Use generator function

# Normal function
def numb(a):
    for i in range(1,a+1):
        print(i)

numb(10)





# Generator function
def numbs(a):
    for i in range(1,a+1):
        yield i

print(numbs(10))

number = numbs(10) # ekbar generate hoise so 2 bar use hbe na

for i in number:
    print(i)

for i in number:   # already happend
    print(i)




number1 = list(numbs(10)) # Because it is list
for i in number1:
    print(i)

for i in number1:   # already happend
    print(i)








# practice evens
def even_generator(a):
    for i in range(1,a):
        if i%2==0:
            yield i
        
for i in even_generator(21):
    print(i)

for i in even_generator(21):
    print(i)

print("\n\n")


# See Difference
def even_generator(a):
    for i in range(1,a):
        if i%2==0:
            yield i

x = even_generator(21)      # ------------------------ #   
for i in x:
    print(i)

for i in x:
    print(i)














# Generator-Function : A generator-function is defined like a normal function,
# but whenever it needs to generate a value, it does so with the yield keyword
# rather than return or print somethings. If the body of a def contains yield,
# the function automatically becomes a generator function.

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 







# A Python program to demonstrate use of  
# generator object with next()  
  
# A generator function 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(next(x)) # In Python 3, __next__() 
print(next(x)) 
print(next(x)) 






# A simple generator for Fibonacci Numbers 
def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
x = fib(5) 
  
# Iterating over the generator object using next 
print(next(x)) # In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
  
# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop") 
for i in fib(5):  
    print(i) 
    
    
    
# -------------------------List vs Generator---------------------------------

# check time and in the Task manager "Memory increasing"

import time

t1= time.time()
l=[i**2 for i in range(10000000)]
print(time.time()-t1)


t2= time.time()
g=(i**2 for i in range(10000000))
print(time.time()-t2)

# and than check time and in the Task manager "Memory increasing"


# --------------------------- Generator Comprehension------------------------

square1 =  ( i**2 for i in range(1,11))
print(square1)
for i in square1:
    print(i)

for i in square1:
    print(i)




# Example
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)








