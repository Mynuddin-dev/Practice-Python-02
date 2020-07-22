# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:41:31 2020

@author: Mynuddin

dictionary = {key: value for vars in iterable}

"""

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)


square={num:num**2 for num in range(1,11)}
print(square)

# for k,v in square.items():
#     print(f"{K} : {v}")
        



#word count
string="MD MYNUDDIN"
word_count={char : string.count(string) for char in string}
print(word_count)




# if use in Dictionary comprehension 
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)



# Odd Even  if else in comprehension
odd_even={i : "Even" if i%2==0 else "Odd" for i in range(1,11)}
print(odd_even)





original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young') for (k, v) in original_dict.items()}
print(new_dict_1)








#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)





#-----------Nested Dictionary with Two Dictionary Comprehensions------------
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)


#same
dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(dictionary)













