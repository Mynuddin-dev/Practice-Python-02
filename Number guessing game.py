# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:32:13 2020

@author: Mynuddin
"""
wining_number=59
guess=1
number=int(input("Enter an intiger value between 1 to 100:"))

while True:
    if number==wining_number:
        print(f"Yea you win and after {guess} time trying")
        break
    else:
        if number<wining_number:
            print("Too low")
            number=int(input("Please guess again:"))
            guess +=1
        else:
            print("Too High")
            number=int(input("Please guess again:"))
            guess +=1






""" DRY -> Dont repeat yourself"""
#-------------vv-----------------
#-------------vv-----------------
#-------------vv-----------------
#-------------vv-----------------



#geeksforgeeks
import random 
  
print("--------------------Number guessing game----------------------") 
  # randint function to generate the  
# random number b/w a to b  

number = random.randint(1, 100) 
chances = 0  
print("############ Guess a number (between 1 and 100) ##############")  
  
# While loop to count the number 
# of chances 
while chances < 10:  
    guess = int(input("Guess a number : ")) 
 
    if guess == number: 
        print(f"Congratulation YOU WON!!! After {chances} time trying") 
        break
    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 
           
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
    chances += 1
    
    
if chances > 10: 
    print("YOU LOSE!!! The number is", number) 
        
        
        
        
        
        
        
        
        
        
        