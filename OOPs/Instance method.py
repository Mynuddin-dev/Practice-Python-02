# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:41:53 2020

@author: Mynuddin
"""
class Person:
    def __init__(self,fname , lname , age):
        #instance variables
        self.fname = fname
        self.lname = lname
        self.age = age
     
    def fulname(self):# instance method
        return f"{self.fname }{self.lname}"
    
    def is_above(self):     #instance method work for every instance or object
        return self.age>18
    
    
    
    
    
P1 = Person("Mynuddin ","Hasan",21)
P2 = Person("Tanzia islam ","Mim",20)

print(P1.fulname())
print(P2.fulname())

print(Person.fulname(P1))   # P1----> self as an object
print(Person.fulname(P2))

print(P1.is_above())



l=[1,2,3,4]  # here l is an object of List  

# lets clear or pop method
print(l.pop())
print(list.pop(l))
#list predefine class
list.append(l,10)
print(l)





#exercise 190

class Computer:
    def __init__(self,b_name,m_name,Price):   
        # instance variables
        self.brand_name=b_name
        self.model_name = m_name
        self.Price = Price
        #self.brand_mpdel_name= b_name , m_name  youcan also do it
         
        
    def percentage(self,num):
        off_price = (num/100)*self.Price
        return self.Price - off_price
    
    # def percentage1(self):
    #     return self.Price - (10/100)*self.Price
        
 
comp1=Computer("HP","corei5 8GB 1TB HDD",63000)    
comp2=Computer("ASUS","corei7 16GB 1TB HDD",83000)

print(comp1.brand_name , comp1.model_name ,comp1.Price,"TK")

print(comp1.percentage(10))
print(comp2.percentage(10))

#print(comp1.percentage1())





