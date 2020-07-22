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
























