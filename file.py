# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:07:24 2018

@author: class
"""
import math
import os
import numpy as np
import random

a=[]
p=1
print("Введи размер массива ")
n = int(input ())
new = np.random.randint(1,100,n)
a.append(new)
print(a)     

for i in range(n):
    p=p*new[i]
p=p**(1/n) 
print("Среднее геометрическое: ")   
print(p)

p2=np.sum(a)
p2=p2/n 
print("Среднее арифметическое: ")   
print(p2) 
