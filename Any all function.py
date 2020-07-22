# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:20:22 2020

@author: Mynuddin
"""
# evens1=[2,4,6,8,10]
# odds1=[1,3,5,7,9]


even=[]
for i in evens1:
    even.append(i%2==0)
print(even)

print(all([True, True, True, True, True]))
print(all([True, True, True, True, False]))


print(any([True, True, True, True, True]))
print(any([True, True, True, True, False]))



print(any([x%2==0 for x in evens1]))
print(any([x%2!=0 for x in odds1]))




# Note :after remove varables
evens1=[2,9,6,10]
odds1=[1,3,2,7,9]

print(all([x%2==0 for x in evens1]))
print(all([x%2!=0 for x in odds1]))

print(any([x%2==0 for x in evens1]))
print(any([x%2!=0 for x in odds1]))


























