# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:13:57 2020

@author: Mynuddin
"""
#zip(*iterables)
user_id=[1,2,3,4]
name=["Laka","saka","Baka","Sourob"]

# (1,"Laka"),(2,"saka"),(3,"Baka"),(4,Sourob)

print(list(zip(user_id,name)))
print(set(zip(user_id,name)))
print(dict(zip(user_id,name)))
print(zip(user_id,name))

zipss=zip(user_id,name)
print(zipss)




# lets Unzip it 

u_id,name1=zip(*zipss)
print(u_id)
print(name1) 

u_id,name1=list(zip(*zipss))  
print(u_id)
print(name1)

print(list(u_id))
print(list(name1))





 
names = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
print(zip(names, roll_no, marks))
print(list(zip(names, roll_no, marks)))
print(set(zip(names, roll_no, marks)))

print(dict(zip(names, roll_no, marks)))
#ValueError: dictionary update sequence element #0 has length 3; 2 is required







# Practical Applications 
# Python code to demonstrate the application of  
# zip()  
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ] 

scores = [100, 15, 17, 28, 43 ] 
# printing players and scores. 
for pl, sc in zip(players, scores): 
    print ("Player :  %s   -->  Score : %d" %(pl, sc)) 





#Passing Arguments of Unequal Length

players = [ "Sachin", "Sehwag", "Gambhir", "Dravid" ] 

scores = [100, 15, 17, 28, 43 ] 
# printing players and scores. 
for pl, sc in zip(players, scores): 
    print ("Player :  %s   -->  Score : %d" %(pl, sc)) 





#Passing No Arguments

zipped = zip()
print(zipped)
print(list(zipped))
print(next(zipped))   #StopIteration because its empty




total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')






# Traversing Dictionaries in Parallel

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)





# Exercise

def avarage(*args):
    newlist=[]
    for pair in zip(*args):
        newlist.append(sum(pair)/len(pair))
    return newlist
print(avarage([1,2,3],[4,5,6],[7,8,9])) 

avarage2=lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avarage2([1,2,3],[4,5,6],[7,8,9])) 















