# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:09:34 2020

@author: Mynuddin
"""

for i in range(10):
    print("Hello Programmer",i)


for i in range(5,11):
    print("Hello Programmer",i)


for i in range(5,100,5):  # step argument

    print("Hello Programmer",i)

#exercise
n=int(input("Enter a value:"))
sum=0
for k in range(1,n+1):
    sum=sum+k
print("Sum : ",sum)




#intiger digit sum

l=(input("Enter a value:"))
sum=0
for k in range(len(l)):
    sum=sum+int(l[k])
print("Sum : ",sum)


#intiger digit sum without loop

num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)



#intiger digit sum

l=int(input("Enter a value:"))
sum=0
t=l
for k in range(t):
    r=t%10
    sum=sum+r
    t=t//10
print("Sum : ",sum)



#print each character occurance
name=input("Enter your name:")
tmp=""
for i in range(len(name)):
    if name[i] not in tmp:
        tmp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    


#sting for loop 

name="Ragnar"
for i in name:
    print(i)


name="Ragnar Lathbroak"
for i in name:
    print(i)



n=input("Enter a value:")     #1234 =1+2+3+4
sums=0
for i in n:
    sums=sums+int(i)
print(sums)














