# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:15:43 2020

@author: Mynuddin
"""
#----------------------------- Update a Dictionary--------------------------

Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
Dictionary2 = { 'C': 'Geeks',3:"Is Best for Python" } 
  
print(Dictionary1) 
  
Dictionary1.update(Dictionary2) 
print(Dictionary1) 

Dictionary3={"And":"Python Docs or python.org","C":"Python crash course"}
Dictionary1.update(Dictionary3)
print(Dictionary1)



 


#Update Nested Dictionary
Employee = {  
    'emp1': { 
        'name': 'Lisa',  
        'age': '29', 
        'Designation':'Programmer'
            },  
         'emp2': { 
             'name': 'Steve', 
             'age': '25', 
             'Designation':'HR'
                 } 
             }  
print(Employee)
# updating in the way similar to simple dictionary 
Employee['emp1']['name']='Kate'
  
print(Employee) 





# The above method updates the value for the mentioned key if it is present in 
# the dictionary. """      Otherwise, it creates a new entry---------------""".

#  For example if you want to add a new attribute ‘salary’ for the first employee
 


# adding new key-value pair to first   
# its a static 

Employee['emp1']['salary']= 56000
  
print(Employee) 







#----------------------------updation dynamic---------------------------------
 
# Get input from the user for which  
# employee he needs to update 
empid = input("Employee id :") 
  
# which attribute / key to update 
attribute = input("Attribute to be updated :") 
  
# what value to update 
new_value = input("New value :") 
  
# updation of the dictionary 
Employee[empid][attribute]= new_value 
  
  
print(Employee)     


 




# ------------------------------Using Loop-----------------------------------
test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4, 'geeks' : 6} 
test_dict2 = {'for' : 3, 'geeks' : 5} 
  
# printing original dictionaries 
print("The original dictionary 1 is : " + str(test_dict1)) 
print("The original dictionary 2 is : " + str(test_dict2)) 
  
# Update dictionary with other dictionary 
# Using loop 
for key in test_dict1: 
    if key in test_dict2: 
        test_dict1[key] = test_dict2[key] 
  
# printing result  
print("The updated dictionary is : " + str(test_dict1))  




