# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 08:30:28 2020

@author: Mynuddin

-------Python lambda (Anonymous Functions) | filter, map, reduce----------

In Python, anonymous function means that a function is without a name.
As we already know that def keyword is used to define the normal functions
and the lambda keyword is used to create anonymous functions. It has the
following syntax:

-----------------lambda arguments: expression-------geeksforgeeks follow--

"""

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
print(sum)


# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 
  
g = lambda x: x*x*x 

print(g(7)) 
print(cube(5)) 

print(cube)
print(g)


# Exercise
is_even= lambda x : x%2==0
print(is_even(4))  
print(is_even(5))  


name="Md Mynuddin"
name1=lambda x : x[3:]
print(name1(name))



#lamda with if else
is_even= lambda x :"Even" if x%2==0 else "Odd"
print(is_even(4))  
print(is_even(5))  





# Tracking iteration 

ls=["Maka","Saka","Daka","Laka"]

POS=0
for i in ls:
    print(f"{POS}----------> {i}")
    POS +=1
  
    
  
    
# Tracking iteration  using enumerate function

# syntex ----> enumerate(iterable, start=0)

for posi,val in enumerate(ls) :
    print(f"{posi}----------> {val}")

for posi,val in enumerate(ls,1) :
    print(f"{posi}----------> {val}")






l1 = ["eat","sleep","repeat"] 
s1 = "geek"
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  

print ("Return type:",type(obj1) )
print (list(enumerate(l1)) )        # as a list
  

# changing start index to 2 from 0 
print (dict(enumerate(s1,100)) )    #as  a dictionary
    
    








# How to use map filter and reduce
# http://net-informations.com/python/iq/map.htm and navin raddy

"""---------------------------Filter-----------------------"""
def even(x):
   return x%2==0      

li=[1,2,3,4,5,6,7,8,9,10]    

evens=list(filter(even,li))
print(evens)

    
# Syntex ------>   map(function, iter) 

# lets think about junk of data 
# 1. you will filter first and get need data ,avoid unncessary data
# 2. than apply some operation  with map function
# 3. than apply reduce i will get finally one result
 


li=[1,2,3,4,5,6,7,8,9,10]    

evens=list(filter(lambda x : x%2==0 ,li))
print(evens)

doubles=list(map(lambda n : n*2,evens))
print(doubles)



# List comprehension
doubles2=[i*2 for i in evens]
print(doubles2)



from functools import reduce
operation=reduce(lambda a,b : a+b,doubles)
print(operation) 





