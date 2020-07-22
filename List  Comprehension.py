# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:56:51 2020

@author: Mynuddin

"""

# ------List Comprehensions provide an elegant way to create new lists.--------

# output_list = [output_exp for var in input_list if (var satisfies this condition)]
#Example 1

square=[]
for i in range(1,11):
    
    square.append(i**2)
    
print(square)

# use list comprehension
square2=[i**2 for i in range(1,11)]
print(square2)




# Example 2

negative=[]
for i in range(1,11):
    
    negative.append(-i)
    
print(negative)

negative1=[-i for i in range(1,11)]
print(negative1)





# Example 3
name=["Mynuddin","Nishad","Byzid"]
# name2=["M","N","B"]   thats the out put
name2=[]
for i in name:
    
    name2.append(i[0])  
print(name2)


name3= [i[0] for i in name]
print(name3)



#example 4
name4=[]
for i in name:
    
    name4.append(i[::-1])   #or use reverse method 
print(name4)

name5=[i[::-1] for i in name]
print(name5)






# -----------------List Comprehension with if statement-------------------

# Constructing output list WITHOUT Using List comprehensions 
input_list = list(range(1,21))
  
output_list = [] 
  
# Using loop for constructing output list 
for var in input_list: 
    if var % 2 == 0: 
        output_list.append(var) 
  
print("Output List using for loop:", output_list) 



#Using List comprehensions 
output_list1=[var for var in input_list if var % 2 == 0]
print(output_list1)


odd=[i for i in input_list if i % 2 != 0]
print(odd)





#Exercise 139
def num_to_string(ls):
    return [str(i) for i in ls if (type(i) == int or type(i) == float)]

def num_to_strings(ls):
    return [str(i) for i in ls if (type(i) == list or type(i) == float)]

print( num_to_string([1 , 2 , 3.0 , ["Hello","Python"] , True , False] ))
print( num_to_strings([1 , 2 , 3.0 , ["Hello","Python"] , True , False] ))






#------------------List Comprehension with if else statement--------------

lst=list(range(1,21))

new_lst=[]
for i in lst:
    if i%2==0:
        new_lst.append(i*2)
    else:
        new_lst.append(-i)
print(new_lst)


new_lst1=[i*2 if (i%2==0) else -i for i in lst]   # sudhu if laste use hoy
print(new_lst1)


obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)


# Nested if
num_list = [y for y in range(1,100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

lk=list(range(1,100))
for i in lk:
    if i%2==0:
        if i%5==0:
            print(i)




# ------------------List comprehension with Nested  list-----------------
example=[[1,2,3],[1,2,3],[1,2,3]]
print(example)
new=[]
for i in list(range(3)):
    new.append([1,2,3])
print(new)

new1=[[i for i in range(1,4)] for j in range(3)]
print(new1)






# 2-D List  to one
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
  
flatten_matrix = [] 
  
for sublist in matrix:      # first 
    for val in sublist:     # second 
        flatten_matrix.append(val) 
          
print(flatten_matrix) 



# Nested List Comprehension to flatten a given 2-D matrix 
flatten_matrix = [val for sublist in matrix for val in sublist]
  
flatten_matrix = [val 
                  for sublist in matrix
                  for val in sublist] 

print(flatten_matrix)








# flatten_matrix = [val
#                   for sublist in matrix
#                   for val in sublist]
    






# 2-D List of planets 
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
flatten_planets = [] 
  
for sublist in planets: 
    for planet in sublist: 
          
        if len(planet) < 6: 
            flatten_planets.append(planet)          
print(flatten_planets)



flatten_planets=[ planet for sublist in planets for planet in sublist if len(planet) < 6 ]
print(flatten_planets)

