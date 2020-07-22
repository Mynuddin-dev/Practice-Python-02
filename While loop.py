# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:55:02 2020

@author: Mynuddin
"""
k=1
while k<=10:
    print("Hello Baby",k)
    k+=1


k=1
sum=0
while k<=10:
    sum=sum+k
    k+=1
print("Sum = ",sum)



n=int(input("Enter your desair num:"))
k=1
sum=0
while k<=n:
    sum=sum+k
    k+=1
print("Sum = ",sum)





n=input("Enter your desair num:")
k=0
sum=0
while k<len(n):
    sum=sum+int(n[k])
    k+=1
print("Sum = ",sum)





#sum of your int digit
n=int(input("Enter your desair num:"))
sum=0
t = n

while (t != 0):
    remainder = t % 10;
    sum       = sum + remainder;
    t         = int(t / 10)

print(f"Sum of digits {n} = {sum}")




#count of each character
name="Md Mynuddin"
i=0
tmp=""
while i<len(name) :
    if name[i] not in tmp:
        tmp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i=i+1





from collections import Counter 
  
# initializing string  
test_str = "GeeksforGeeks"
  
# using collections.Counter() to get  
# count of each element in string  
res = Counter(test_str) 
  
# printing result  
print ("Count of all characters in GeeksforGeeks is :\n "+  str(res)) 



https://www.xxxfiles.com/videos/141029/01c9b2a3c77474cb44e7a70a38023245/


i=1
while i<=5:
    print("Mujko Time ",end="")
    j=1
    while j<=4:
        print("Aega ",end="")
        j+=1
    i+=1    
    print()

