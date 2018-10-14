# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:48:17 2018

@author: Tianqi Guo
"""
str = "+-2"
l = len(str)
n = 0.0
nc = "0123456789"

sign = 1
num_start = False
for i in range(l):
    c = str[i]
    if (c == " ") and (not num_start):
        continue
    if (c == "-") and (not num_start):
        sign = -1
        num_start = 1
        continue
    if (c == "+") and (not num_start):
        sign = 1
        num_start = 1
        continue
    digit = nc.find(c)
    if digit != -1:
        num_start = 1
        n = n * 10 + digit
    else:
        break
n = int(n * sign)
n = max(n, -2**31)
n = min(n, 2**31 - 1)
print(n)
        
