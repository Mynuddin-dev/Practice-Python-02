# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:11:38 2020

@author: Mynuddin
"""
# store anything any type of data


ls=[1,2,3,4,95,54]
ls1=["word1","word2", "word3","word4"]
print(ls)
print(ls1)
print(ls[-1])

print(ls[:3])

print(ls[::1])

print(ls[::2])
print(ls[::-1])
ls3=ls+ls1
print(ls3)


ls[:2]=[34,65]
ls[:3]=[34,65,43]
print(ls)

ls1[:]=[34,54,77]

ls1[:]=[34,54,77,32,23]
print(ls1)

print(ls3)
ls3[1:5]=[43]
print(ls3)
ls3[1]=["hello",4]
print(ls3)



#----------------------------methods------------------------------



ls4=[]
ls4.append([3,2,5])
#ls4.append(23,43)  #append() takes exactly one argument (2 given)
ls4.append(43) 
ls4.append(323) 

ls4.insert(1,45)
print(ls4)

ls5=ls+ls1
print(ls5)

a=["veloce","rocket"]
b=["phonix","legion"]
c=["nikro","hero"]
 
a.append(b)   #add as a list
print(a)
b.extend(c)   #add as a value
print(b)

c.sort()
print(c)

d=[9,4,3,2,3,4,5,6,45,65,76,23,54]
d.sort()
print(d)

d.pop()
print(d)

d.pop(3)
print(d)

del d[3]
print(d)

k=[23,34,32,56,78,88,76]
print(k)
del k
print(k)

l=[32,43,545,67,45]
print(l)
l.clear()
print(l)    #please compare to del method
#clear the all value just not del the full list


d.remove(45)
print(d)

#---------------in keyword----------------
if 65 in d:
    print("Present")
else:
    print("Not Present")    

e=[2,425,65,809,98,90]
d.extend(e)
print(d)
d.sort()
print(d)
b.sort()
print(b)

d.count(2)
d.count(3)
d.count(65)
d.count(9)



#----------if you want just print sorted order not sorted the  list-------
print(e)
print(sorted(e))
print(e)

name=d.copy()
print(d,"\n",name)



#----------------------------compare == and is--------------------------- 

A=["aja","aja","mera ","vai"]
B=["aja","aja","mera ","vai"]
C=["aja","aja","mera ","vai","dhat chal ja"]

print(A==B)   #check is their value same or not
print(A is B) #its check is they are same memory location or not 

D=5
E=D
print(D is E)

print(A==C)





#------------------------Split and join method---------------------------

#split method convert string into a list
name="Md Mynuddin khaza".split()
print(name)
name1="1,2,3,4,5,6,78,9".split(",")
print(name1)

n="Mynuddin,24".split(",")
print(n)

np,np1="Mynuddin,24".split(",")
print(np)
print(np1)


#join methon convert list to string
n=["Mynuddin","24"]
print(n)
print(",".join(n))

#------------------------------String vs List-----------------------------

#string is immutable means you cant change 
#List is mutable that means you can change its value

AB="Ivar is the son of Ragnar"
print(AB)
AB.title()
print(AB) 
AB.replace("Ivar", "EMKMKN")
print(AB) 


BC=[2,3,4,5,6]  #changable
BC.pop()
BC[1]=3
print(BC)


#---------------------------loping in list----------------------------------
names=[3,4,3,2,3,4,5]
for i in names:
    print(i,end=" ")

i=0
while i<len(names):
    print(names[i],end=" ")
    i+=1


#--------------------------list inside list--------------------------------=
listt=[[1,2,3],[4,5,6],[7,8,9]]  #as like 2d
print(listt)

for i in listt:
    print(i)

for sublist in listt:
    for i in sublist:
        print(i)
        
print(listt[2][0])  
print(listt[1][1])  



#list using range
num=list(range(1,21))
print(num)

a=num.pop()
print(a)
num.index(5)

num.index(2)

num.append(4)
num.index(4)

num.index(4,5)

num.index(4,5,21) #value start stop

negative=[]
for i in num:
    negative.append(-i)
print(negative)    




#-----------------------creating list as an user input----------------------
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) # adding the element 
      
print(lst) 




#exercise 98

def Square(h):
    sq=[]
    for i in h:
      
        sq.append(i**2)
    return sq

nk=list(range(1,11))    
print(Square(nk))  

    

lk=list(input("Values inserted:").split(" "))
print(lk)    


#Exerxise 100 

def rev(ls):
    return ls[::-1]

AS=list(range(1,11))
print(AS)
print(rev(AS))
    

#Using pop and append method    
lg=[]
def rev(ls):
    
    for i in range(len(ls)):
        lg.append(ls.pop())
rev(AS)    
print(lg)   
    
    
#Exercise 102
def lrev(listts) :
    ele=[]
    for i in listts:
        ele.append(i[::-1])
    return ele

word=["abc","def","efg"] 
print(lrev(word)) 
  



#Exercise 104
def odd_even(ls):
    odd=[]
    even=[]
    for i in ls:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output
            

num=list(range(1,8)) 
print(odd_even(num))
     
 
    
#Exercise 106
def common(ls1,ls2):
    empty=[]
    for i in ls1:
        if i in ls2:
            empty.append(i)
        else:
            pass
    return empty
        
    
    
L1=[1,2,3,9,8,5]
L2=[1,2,7,9,10]   
 
print(common(L1,L2))
print(min(L1))
print(max(L1))
print(min(L2))
print(max(L2))



#exercise 108

LS1=[1,2,3,[3,4],[7,8,9]]
print(LS1)
print(len(LS1))
print(type(LS1))







