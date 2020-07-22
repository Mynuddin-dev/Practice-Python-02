# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:31:19 2020

@author: Mynuddin
"""
# Tuple is data structure 
# Tuple store any type of data structure
# tuples use parentheses, whereas lists use square brackets.
#tuple is immutable unlike lists which are mutable. once you created you cant update

Example=("one" ,"two","three")

# No append , No pop , No remove ,No insert just no change 
#tuple are faster than list

print(Example)



# An empty tuple 
empty_tuple = () 
print (empty_tuple)



# Tuple with one element
T=("Mynuddin")
T1=(7)
print(T)
print(type(T))
print(T1)
print(type(T1))

t1=(3,)
print(t1)
print(type(t1))

t=("Mynuddin",)
print(t)
print(type(t))



# One way of creation 
tup = 'python', 'geeks',4,8.0
print(tup) 
print(type(tup))
# Another for doing the same 
tup = ('python', 'geeks') 
print(tup)



# Tuple unpacking
guiter=("ragnar","peri","Malika")
guiter1,guiter2,guiter3=(guiter)
print(guiter1)



# list inside Tuple
fav=("Malkova","Denni","alex Texas",[32,36,65,"Lagartha" , "Lathbroak"])
print(fav)

fav[3].pop()
print(fav)
fav[3].append("Bjorn")
print(fav)    #list method applicable




#Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

print(tup1+tup2)





# Code for creating nested tuples 
  
tuple1 = (0, 1, 2,3,3) 
tuple2 = ('python', 'geek') 
tuple3 = (tuple1, tuple2) 
print(tuple3)

print(tuple1.index(2))
print(tuple1.count(3))





# Code to create a tuple with repetition 
tuple4 = ('python',)*3
print(tuple4)




#code to test that tuples are immutable 
tupl = (0, 1, 2, 3) 
tupl[0] = 4
print(tupl)





# code to test slicing tuple
tuple1 = (0 ,1, 2, 3) 
print(tuple1[1:]) 
print(tuple1[::-1]) 
print(tuple1[2:4]) 




# Negative indexing for accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
# Output: 't'
print(my_tuple[-1])
# Output: 'p'
print(my_tuple[-6])

print(min(tuple1))
print(max(tuple1))






# Code for deleting a tuple 
tuple3 = ( 0, 1) 
del tuple3 
print(tuple3) 




# Code for printing the length of a tuple 
tuple2 = ('python', 'geek') 
print(len(tuple2))




num=tuple(range(1,11))
print(num)

num1=list(num)
print(num2)
print(type(num1))

num2=str(num1)
print(num2)
print(type(num2))





# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)





#Converting list to a Tuple
# Code for converting a list and a string into a tuple 

list1 = [0, 1, 2] 
print(tuple(list1)) 
print(tuple('python')) # string 'python' 

#Takes a single parameter which may be a list,string,set or even a 
#dictionary( only keys are taken as elements) and converts them to a tuple.






# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)





#python code for creating tuples in a loop 
tup = ('geek',) 
n = 5  #Number of time loop runs 
for i in range(int(n)): 
    tup = (tup,) 
    print(tup)


for i in tup:
    print(i)


