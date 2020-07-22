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







# -----------------------------class variable-----------------------------


class Computer:
    
    percent =10      # class variable --> sharable for every object
    
    def __init__(self,b_name,m_name,Price):  
        
        # instance variables difference for every object 
        
        self.brand_name=b_name
        self.model_name = m_name
        self.Price = Price
        #self.brand_mpdel_name= b_name , m_name  youcan also do it
         
        
    def percentage(self):
        off_price = (Computer.percent/100)*self.Price
        return self.Price - off_price
    
    # def percentage1(self):
    #     return self.Price - (10/100)*self.Price
        
 
comp1=Computer("HP","corei5 8GB 1TB HDD",63000)    
comp2=Computer("ASUS","corei7 16GB 1TB HDD",83000)

print(comp1.brand_name , comp1.model_name ,comp1.Price,"TK")

print(comp1.percentage())

print(comp1.__dict__)











# Another Example
 
class Circle:
    
    pi=3.1415 # class variable --> sharable for every object

    def __init__(self,radious):
        self.radious=radious
        
    def area(self):
        return (2*self.radious*Circle.pi)

c1 = Circle(10)
c2 = Circle(20)

print(c1.area())
print(c2.area())










# Another Example  from Navin

class Employee:
    increment=1.5      #class variable   ---> sharable 
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname  
        self.lname=lname
        self.salary=salary
        self.increment=1.4    #instance variable
        Employee.no_of_employee +=1
        
    def increase(self):
        #self.salary = self.salary*Employee.increment #use class variable
        #self.salary = self.salary*self.increment      #first search in instance
                                                      #variable if not find take
                                                      #class variable

        self.salary = self.salary*self.increment
print(Employee.no_of_employee)
harray=Employee("Harry","Potter",44000)
print(Employee.no_of_employee)
rohan=Employee("Rohan","Sharma",55000)    
print(Employee.no_of_employee)

 
print(harray.salary)
harray.increase()
print(harray.salary)   

print(harray.__dict__)  #instance variable print  
print(rohan.__dict__)




# As like above
class Computer:
    
    percent =10      # class variable --> sharable for every object
    
    def __init__(self,b_name,m_name,Price):  
        
        # instance variables difference for every object 
        
        self.brand_name=b_name
        self.model_name = m_name
        self.Price = Price
        self.percent=20        # first check it      
        
    def percentage(self):
        off_price = (self.percent/100)*self.Price
        return self.Price - off_price
    
    # def percentage1(self):
    #     return self.Price - (10/100)*self.Price
        
 
comp1=Computer("HP","corei5 8GB 1TB HDD",63000)    
comp2=Computer("ASUS","corei7 16GB 1TB HDD",83000)
 
print(comp1.percentage())

