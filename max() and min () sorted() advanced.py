# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:10:00 2020

@author: Mynuddin
"""

print (max( 4,12,43.3,19,100 ) ) 
print (min( 4,12,43.3,19,100 ) ) 


# lexicographically largest and smallest of Strings i.e String appearing first in dictionary or last.
print (max( "geeks", "manjeet", "algorithm", "programming" ) ) 
print (min( "geeks", "manjeet", "algorithm", "programming" ) ) 


l= ["ab", "abc", "abd", "b"]  
l1="abc"
# prints 'b' 
print(max(l)) 
# prints 'ab' 
print(min(l)) 
#prints 'c' 
print(max(l1)) 
#prints 'a' 
print(min(l1))
# output comes according to lexicographical order



#------------------Syntax: max(x1, x2, ..., xn, key=function_name)---------

# here x1, x2, x3.., xn passed arguments
# function_name : denotes which type of operaton you want to perform on 
# these arguments. Let function_name=len, so now output gives according to 
# length of x1, x2.., xn.


l = ["ab", "abc", "bc", "c"] 
  
print(max(l, key = len)) 
print(min(l, key = len))


# initally l = [“ab”, “abc”, “bc”, “c”]
# when we passed key=len as arguments then it works like
# l=[2,3,2,1]


def fun(element): 
    return(len(element)) 
  
l =["ab", "abc", "bc", "c"] 
print(max(l, key = fun)) 
  
# you can also write in this form 
print(max(l, key = lambda item : len(item))) 



# Another Example

l = [{'name':'ramu', 'score':90, 'age':24}, 
     {'name':'golu', 'score':70, 'age':19},
     {'name':'cholu', 'score':97, 'age':23}
     ] 
  
# here anonymous function takes item as an argument. 
print(max(l, key = lambda item : item.get('age'))) 
print(max(l, key = lambda item : item['age'])) 

print(min(l, key = lambda item : item.get('age'))) 
print(max(l, key = lambda item : item.get('score'))) 
print(min(l, key = lambda item : item.get('score'))) 

print(min(l, key = lambda item : item.get('score'))['name']) 



print(sorted(l, key = lambda item : item.get('age'))) 
print(sorted(l, key = lambda item : item['score'])) 
print(sorted(l, key = lambda item : item['score'] , reverse=True ))
reverse = sorted(l, key = lambda item : item['score'] , reverse=True )
print(reverse)






# # its dictionary
# student2 = { 
#      'Aamu' : {'score':90, 'age':24}, 
#      'Bolu' : {'score':70, 'age':19},
#      'Jholu': {'score':97, 'age':23}
#      }

# print(max(student2, key = lambda item : student2[item]['score']) 



name=["Harshit","Byzid","Mynuddin", "Mizan"]
print(max(name,key=len))
print(min(name,key=len))


# jdi soman hoy maintain lexigraphically order
names=["Harshhit","Byzid","Mynuddin", "Mizan"]
print(max(names,key=len))
print(min(names,key=len))





































