# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:43:21 2020

@author: Mynuddin

 When a for loop is executed, for statement calls iter() on the object,
 which it is supposed to loop over. If this call is successful, 
 the iter call will return an iterator object that defines the 
 method __next__(), which accesses elements of the object one at a time.
 The __next__() method will raise a StopIteration exception, if there are 
 no further elements available. The for loop will terminate as soon as it
 catches a StopIteration exception

"""
numbers=[1,2,3,4,5,6]   #list Set Tuple Dictionary Iterables


square= map(lambda i:i*2 ,numbers)     #Iterator


print(numbers)
print(square)

for i in numbers:
    print(i)
    
num=iter(numbers) #the iter call will return an iterator objec 

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num)) 
print(next(num))



print(iter(numbers)) #the iter call will return an iterator objec 

print(next(numbers))

#in interator you can call directly 
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))

# Note: If ‘next(iterator_obj)’ is called one more time, it would return ‘StopIteration’.







# Geeksforgeeks
for city in ["Berlin", "Vienna", "Zurich"]: 
    print(city) 
  
print("\n") 
      
for city in ("Python", "Perl", "Ruby"): 
    print(city) 
  
print("\n") 
      
for char in "Iteration is easy": 
    print(char, end = " ") 




cities = ["Berlin", "Vienna", "Zurich"] 
  
# initialize the object 
iterator_obj = iter(cities) 
  
print(next(iterator_obj)) 
print(next(iterator_obj)) 
print(next(iterator_obj)) 



#Check object is iterable or not
# Function to check object 
# is iterable or not  
def iterable(obj): 
    try: 
        iter(obj) 
        return True
          
    except TypeError: 
        return False
  
# Driver Code      
for element in [34, [4, 5], (4, 5), 
             {"a":4}, "dfsdf", 4.5]: 
                   
    print(element, " is iterable : ", iterable(element)) 










