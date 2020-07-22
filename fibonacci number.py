# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:24:45 2020

@author: Mynuddin
"""
# 0 1 1 2 3 5
#Space Optimized method

def fibonacchi(n):
    first=0
    second=1
    if n<0:
        print("sorry Incorrect input")
    elif n==0:
        print(first, end=" ")
    elif n==1:
        print(second, end=" ")
    else:
        print(first ,second,end=" ")
        
        for i in range(n-2): 
            tmp=first+second
            first=second
            second=tmp
            print(second,end=" ")
            
fibonacchi(int(input("Please Enter a value:")))          
            




def fibonacchi(n):
    f=0
    s=1
    if n<0:
        print("sorry Incorrect input")
    elif n==0:
        print(f, end=" ")
    elif n==1:
        print(s, end=" ")
    else:
        print(f,s,end=" ")
        
        for i in range(n-2): 
            next=f+s                           
            print(next,end=" ")
            f=s
            s=next
            
fibonacchi(int(input("Please Enter a value:")))          
            



#using recursion

def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  
   
nterms = int(input("Enter the terms? "))  # take input from the user
  
if nterms <= 0:  # check if the number is valid 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(FibRecursion(i) , end=" ")




