# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 06:12:08 2020

@author: Mynuddin
"""
class Person:
    def __init__(self,fnam , lname , age):
        #instance variables
        print("__init__ method / constructor getting called")
        self.fnam = fnam
        self.lname = lname
        self.age = age
    
    
    # def __init__(person_instance,fnam , lname , age):
    #     #instance variables
    #     print("__init__ method / constructor getting called")
    #     person_instance.fnam = fnam
    #     person_instance.lname = lname
    #     person_instance.age = age
    
P1 = Person("Mynuddin","Hasan",21)
P2 = Person("Tanzia islam","Mim",20)

# print(P1.fnam ,"---->", P2.fnam)
print(P1.fnam)
print(P2.fnam)
print(P1.age)





# Exercise 187
class Computer:
    def __init__(self,b_name,m_name,Price):   
        self.brand_name=b_name
        self.model_name = m_name
        self.Price = Price
        #self.brand_mpdel_name= b_name , m_name  youcan also do it

comp1=Computer("HP","corei5 8GB 1TB HDD",63000)    
comp2=Computer("ASUS","corei7 16GB 1TB HDD",83000)

print(comp1.brand_name , comp1.model_name ,comp1.Price,"TK")

# print(comp2.brand_mpdel_name)
#print(type(comp2.brand_mpdel_name))
