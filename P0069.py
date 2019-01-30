# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:43:51 2019

@author: Tianqi Guo
"""

x = 0

x = float(x)
a = x
flag = True
while flag:
    b = (a + x/a)/2 
    flag = (int(a) != int(b))    
    a = b   

print a
    
    
