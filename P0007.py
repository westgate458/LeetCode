# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:13:24 2018

@author: Tianqi Guo
"""

x = 1534236469
y = 0
while x != 0:
    x0 = x
    x = int(float(x) / 10)
    d = x0 - x * 10    
    y = y * 10 + d
    
if y < - 2**31 or y > 2**31 - 1:
    y = 0
    
print(y)