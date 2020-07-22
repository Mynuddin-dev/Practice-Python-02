# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 21:50:46 2020

@author: Mynuddin
"""

def square(a):
    return a**2

print(square(7))
s = square
print(s(7))

print(s.__name__)
print(square.__name__)
print(s)               #same location
print(square)          #same location








# Passing Functions as Arguments to other Functions
def square(a):
    return a**2 

l=[1,2,3,4,5]
print(list(map(square,l)))
print(list(map(lambda x : x**2 ,l)))
 
 
def mymap(func , l):
    nl=[]
    for item in l:
    
        nl.append(func(item))
    return nl

print(mymap(square , l))

print(list(mymap(lambda x : x**2 ,l)))

print(list(mymap(lambda x : x**3 ,l)))



def mymap2(func , l):
    return [func(item) for item in l]

print(list(mymap2(lambda x : x**4 ,l)))





# Functions Returning other Functions

def outer_func():
    def inner_func():
        print("Inside Inner function execute")
    #return inner_func
    return inner_func()


var =outer_func()
# var = outer_func()
# var
# var()



def outer_func2(msg):
    def inner_func2():
        print(f"The message is :{msg}")
    return inner_func2


var2 =outer_func2("Assalamu Alaikum")
var2()




# clouser or first class function
# # Functions Returning other Functions(closure)
def to_power(n):
    def calc(x):
        return x**n
    return calc
    
cube =to_power(3)
print(cube(5))

square2=to_power(2)
print(square(5))

square1= to_power(2)(5)
print(square1)







# Nested Functions have access to the Enclosing Function's Variable Scope
def print_message(message):
    #print("Enclosong Function")
    def message_sender(): 
        #print("Nested Function")
        print(message)
    message_sender() 

print_message("Some random message")











# Decorators  enhance the functionality of other functions

def decorator_function(any_function):
    def wrapper_function():
        print("This is from decorator and its awsome ,increase functionality")
        any_function()
        #return 1
    return wrapper_function 


def func1():
    print("This is function 1")
    # wanna be print "This is from decorator and its awsome ,increase functionality"
   
    
def func2():
    print("This is function 2")
    # wanna be print "This is from decorator and its awsome ,increase functionality"
   

# func1 = decorator_function(func1)
# func1()
var2 = decorator_function(func1)
var2 = decorator_function(func2)
var2()
print(var2())    
     
    
    


#  use @ decorator or syntactic sugar 
 

def decorator_function(any_function):
    def wrapper_function():
        print("This is from decorator and its awsome ,increase functionality")
        any_function()
    return wrapper_function 

@decorator_function
def func1():
    print("This is function 1")
    # wanna be print "This is from decorator and its awsome ,increase functionality"
func1()    
    
@decorator_function
def func2():
    print("This is function 2")
    # wanna be print "This is from decorator and its awsome ,increase functionality"
func2()  
 

 



# problem occurs
def decorator_function(any_function):
    def wrapper_function():
        print("This is from decorator and its awsome ,increase functionality")
        any_function()
    return wrapper_function 

@decorator_function
def func3(a):
    print("This is function 3 with arghument :",a)

func3(7)
# TypeError: wrapper_function() takes 0 positional arguments but 1 was given
    




# solution
def decorator_function(any_function):
    def wrapper_function(*args ,**kwargs): 
        print("This is from decorator and its awsome ,increase functionality")
        any_function(*args ,**kwargs)
    return wrapper_function 


@decorator_function 
def func3(a):
    print("This is func3 with arghument :",a)

func3(7)
print(add.__name__)








# problm and solution
def decorator_function(any_function):
    def wrapper_function(*args ,**kwargs): 
        
        """This is Wrapper function"""
        
        print("This is from decorator and its awsome ,increase functionality")
        #any_function(*args ,**kwargs)
        return any_function(*args ,**kwargs)
    return wrapper_function 


@decorator_function
def add(x,y): 
    """This is add function"""
    return x+y 
print(add(5,4))

print(add.__name__)
print(add.__doc__)   #problem occurs




# solution
from functools import  wraps
def decorator_function(any_function):
    
    @wraps(any_function)
    def wrapper_function(*args ,**kwargs): 
        
        """This is Wrapper function"""
        
        print("This is from decorator and its awsome ,increase functionality")
        #any_function(*args ,**kwargs)
        return any_function(*args ,**kwargs)
    return wrapper_function 



@decorator_function
def add(x,y): 
    """This is add function"""
    return x+y 
print(add(5,4))

print(add.__name__)
print(add.__doc__)   #problem solved





# practice 174
from functools import wraps
import  time
t1=time.time()
def deco(anyfunc):
    @wraps(anyfunc)
    def wrap(*args,**kwargs):
        print(f"You are calling {anyfunc.__name__} function")
        print(f"{anyfunc.__doc__}") 
        return anyfunc(*args,**kwargs)
    return wrap
 


@deco
def addition(a,b):
    """This function takes two number as a argument and return their sum"""
    return a+b
    
print(addition(4,8))
t2=time.time()
print(t2-t1)
















