# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:26:48 2020

@author: Mynuddin

"""
# class methods access class variable not instance variable
# but instance methods access  insatance and class variable
# Class methods can be called by both class and object
# A class method is a method which is bound to the class and not the object of the class.


# class method related to the class
# instance methods related to the instance(object)
# static method as like normal method directly not connected class or object



class Person:
    
    instance = 0
    
    def __init__(self,fname , lname , age):
        #instance variables
        Person.instance +=1
        self.fname = fname
        self.lname = lname
        self.age = age
        
    @classmethod
    def cl_method(cls):
        return f"You have created {cls.instance} instance of {cls.__name__} class"
        
     
        
    def fulname(self):# instance method
        return f"{self.fname }{self.lname}"
    
    def is_above(self):    
        return self.age>18
    
    
P1 = Person("Mynuddin ","Hasan",21)
P2 = Person("Tanzia islam ","Mim",20)

print(Person.cl_method())   #recommended
print(P1.cl_method())






# class method as a constructor


class Person:
    
    instance = 0
    
    def __init__(self,fname , lname , age):
        #instance variables
        Person.instance +=1
        self.fname = fname
        self.lname = lname
        self.age = age
        
    @classmethod
    def from_string(cls,string):
        fname,lname,age=string.split(",")
        return cls(fname,lname,age)
        
    
    @classmethod
    def cl_method(cls):
        return f"You have created {cls.instance} instance of {cls.__name__} class"
        
     
        
    def fulname(self):# instance method
        return f"{self.fname }{self.lname}"
    
    def is_above(self):    
        return self.age>18
    
    
P1 = Person("Mynuddin ","Hasan",21)
P2 = Person("Tanzia islam ","Mim",20)

P3 =Person.from_string("Md Mynuddin,Khaza,21")

print(P3.age)

print(Person.cl_method())   #recommended






class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method 
Person.printAge = classmethod(Person.printAge)

Person.printAge()


















