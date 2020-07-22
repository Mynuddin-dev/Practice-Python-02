# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:58:30 2020

@author: Mynuddin
"""
"""-------------------------------   SET   ------------------------------------"""

# However, a set itself is mutable. We can add or remove items from it.
# must be immutable (cannot be changed).
# Unordered collections of unique elements ...


s={1,2,3,4,5}
print(s)
s={1,2,3,4,3,3,2,1,5}
print(s)

print(s[4])   # cant access bcause of unordered collection



#Remove duplicates
l=[12,23,34,56,78,12,23,67,67]
print(l)
print(list(set(l)) )



# add value
s1={1,2,3,49,3,7}
print(s1)
s1.add(6)
print(s1)
s1.add(7)
print(s1)


#m Remove
s1.remove(49)
print(49)



## pop method
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
print(my_set.pop())
print(my_set)


s1.remove(5)     #KeyError
s1.discard(3)
print(s1) 
s1.discard(9)    # if not find dont show any error
print(s1)



#clear method
s1.clear()
print(s1)



# Copy method
s2={9,8,5,6,7}
print(s2)
s3=s2.copy()
print(s3)


# cant store list and Dictionary 
# except this you can store anythings
se={1,2,2.3,3.5,"Hello",(2,3,4,5)}
print(se)

se1={"1":"E",[2,3,4,4]}       # Error
print(se1)

print(1 in se)
print("Hello" in se)

for item in se:
    print(item)




# Union and Intersection

sets1={1,2,3,4,5}
sets2={3,4,5,6,7}

print(sets1 |sets2)
print(sets1 & sets2)

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))
print(B.union(A)) 

print(A.intersection(B))
print(B.intersection(A))





# Set Difference in Python
print(A - B) 
print(A.difference(B))

print(B-A)
print(B.difference(A))



 
# https://www.programiz.com/python-programming 
# symmetric_difference()
print(A ^ B)
print(A.symmetric_difference(B)) 
print(B.symmetric_difference(A))





# Distinguish set and dictionary while creating empty set
# initialize a with {}
a = {}
# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))




