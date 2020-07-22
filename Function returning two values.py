# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:19:16 2020

@author: Mynuddin
"""

def add_mul(a,b):
    return a+b,a-b

print(add_mul(6,2)) # Tuple

A,B=add_mul(6,3)
print(A,B)