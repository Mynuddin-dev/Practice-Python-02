# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 07:26:20 2020

@author: Mynuddin
"""
# Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized.
#Dictionary in Python is an unordered collection of data values

# Values in a dictionary can be of any datatype and can be duplicated, 
# whereas keys can’t be repeated and must be immutable.



# Creating a Dictionary  
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 


#Method 1
Dict2={"Name":"Md mynuddin","Age":21,"Work":"Programing"}
print(Dict2)




# with dict() method  4
Dict = dict({1: 'Geeks', 2: 'For', "t":'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 



# Method 2
Dict3=dict(Name="Md Mynuddin",Age=21, Work="Programing")
print(Dict3)



# Meethod 3
Dict4=dict([("Name","Md Mynuddin"),
           ("Age",21), 
           ("Work","Programing")])

print(Dict4)
print(type(Dict4))



MLB_team = {
    
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers', 
    'Seattle'  : 'Mariners',
    'fav_movie':['Forest gump','The shawsank Redeption'],
    
    'fav_food' :['Biriyani','vagitable','Minarel Water','Biri']}

print(MLB_team)



# Creating a Nested Dictionary  
Dict5 = {1: 'Geeks',
         2: 'For',  
         3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'},
         4:[3,2,3]} 
  
print(Dict5) 




#Empty List
#-----------------------Adding elements to a Dictionary--------------------


Empty={}
print(Empty)

Empty["Name"]="Md Mynuddin"
print(Empty)
Empty["Age"]=45
print(Empty)


Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  

# Adding set of values  
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
print(type(Dict["Value_set"]))  

 
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
  

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 






#------------------Accessing elements from a Dictionary--------------------



#cant access elements by indexing bcause of unordered
print(MLB_team[0])   # KeyError  line 58


#In order to access the items of a dictionary refer to its key name.
#Key can be used inside square brackets.

# MLB_team = {
    
#     'Colorado' : 'Rockies',
#     'Boston'   : 'Red Sox',
#     'Minnesota': 'Twins',
#     'Milwaukee': 'Brewers', 
#     'Seattle'  : 'Mariners',
#     'fav_movie':['Forest gump','The shawsank Redeption'],
    
#     'fav_food' :['Biriyani','vagitable','Minarel Water','Biri']}

# print(MLB_team)

Dict7 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
# accessing a element using key 
print("Accessing a element using key:") 
print(Dict7['name']) 
print(Dict7[1]) 

print(MLB_team["Seattle"])
print(MLB_team.get("Boston"))
print(MLB_team.get("Hei")) #mot error


print(MLB_team.keys())
print(MLB_team.values())
print(MLB_team.items())

# check for keys
print('Colorado' in MLB_team)
print('ABC' in MLB_team)

# check for values
print('Red Sox' in MLB_team.values())
print('Mariners' in MLB_team.values())
print(['Forest gump','The shawsank Redeption'] in MLB_team.values())





#------------------------ Loops in Dictionary------------------------------



for i in MLB_team:
    print(i)
    
for i in MLB_team.keys():
    print(i)

for i in MLB_team:
    print(MLB_team[i])

for i in MLB_team.values():
    print(i)

for i in MLB_team.items():
    print(i)

for i,j in MLB_team.items():
    print(i," : ",j)
    
for key,value in MLB_team.items():
    print(key," : ",value)
    
print(type(MLB_team.keys()))
print(type(MLB_team.values()))




#------------------- Accessing element of a nested dictionary----------------


Dict8 = {"Dict1": {"fn": 'Geeks', "mn":"Geeks" }, 
        "Dict2": {"ls": "For"}} 
  
# Accessing element using key 
print(Dict8['Dict1']) 
print(Dict8['Dict1']["fn"]) 
print(Dict8['Dict2']['ls']) 


print(MLB_team["fav_movie"]) 
print(MLB_team["fav_food"])




# ---------------------Removing Elements from Dictionary--------------------



Dict9 = {5 : 'Welcome', 
        6 : 'To', 
        7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}
       } 

print("Initial Dictionary: ") 
print(Dict9) 
  
# Deleting a Key value 
del Dict9[6] 
print("\nDeleting a specific key: ") 
print(Dict9) 
  
# Deleting a Key from 
# Nested Dictionary 
del Dict9['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict9) 

#Using pop() method
#Pop() method is used to return and delete the valsue of the key specified.
k=Dict9.pop(5)                 #Return A list
print("Poped item:" ,k)


Dick = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
print(Dick)
pop_ele = Dick.popitem()      # compare to pop()  Return a Tuple
print(pop_ele)
print(Dick)

Dick.clear()
print(Dick)






#--------------------------------Copy--------------------------------------


d={1:"A",2:"B",3:"C",4:"D"}
print(d)

d1=d.copy()   #shallow copy
d.pop(1)
print(d1)
print(d)

# check after Removing variables
d2=d          #deep copy  
d.pop(2)
print(d2)
print(d)






#---------------------------fromkeys() method------------------------------

# The fromkeys() method creates a new dictionary from the given sequence of
# elements with a value provided by the user.
#dictionary.fromkeys(sequence[, value])

#sequence - sequence of elements which is to be used as keys for the new dictionary
#value (Optional) - value which is set to each each element of the dictionary


# initializing sequence  
seq = { 'a', 'b', 'c', 'd', 'e' } 
# using fromkeys() to convert sequence to dict  
# initializing with None 
res_dict = dict.fromkeys(seq)
print(res_dict) 



# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)




#Create a dictionary from mutable object list
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1] 
vowels = dict.fromkeys(keys, value)
print(vowels) 

# updating the value
value.append(2)
print(vowels)



seq = { 'a', 'b', 'c', 'd', 'e' } 
lis1 = [ 2, 3 ] 
rest_dict = dict.fromkeys(seq, lis1) 
# Printing created dict 
print (rest_dict) 
  
# appending to lis1 
lis1.append(4) 
print(rest_dict)



print(dict.fromkeys(range(1,11)))
print(dict.fromkeys(range(1,11),"A"))






#-----------if in Dictionary two key are same at the same time they cant------

a=[1,2,3,4,5]
b=["A","B","C","D","E"]
print(dict.fromkeys(a,b))

c={1:"A",2:"B",3:"C"}
print(c)
c={1:"A",2:"B",3:"C",3:"D"}  #count last value 
print(c)






#exercise 123
def cube(n):
    AB={}
    for i in range(1,n+1):
        AB[i]=i**3
    return AB

print(cube(10))




#exercise 125 --> letter  count

def wc(st):
    word={}
    for char in st:
        word[char]=st.count(char)
        
    return word
print(wc('Md Mynuddin'))
    

#Exercise 127 --> Dictionary user input

Dicks={}
name=input("Enter your name:")
age=input("Enter your age:")
Movie=input("Enter your movie use comma:").split(",")
Food=input("Enter your Food use comma:").split(",")

Dicks["Name"]=name
Dicks["Age"]=age
Dicks["Movies"]=Movie
Dicks["Foods"]=Food 

for k,v in Dicks.items():
    print(f"{k} : {v}")







