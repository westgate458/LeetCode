# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:06:12 2018

@author: Tianqi Guo
"""

s = "ab"
p = ".*"

ls = len(s)
lp = len(p)

match = [[False] * (lp+1) for i in range(ls+1)]
match[0][0] = True

for j in range(1,lp+1):
    c_p = p[j-1]
    if c_p == '*':
        match[0][j] = match[0][j-2]   

for i in range(1,ls+1):
    for j in range(1,lp+1):
        
        c_s = s[i-1]
        c_p = p[j-1]
        c_match = (c_p == '.') or (c_s == c_p);
        
        if c_match and match[i-1][j-1]:
            match[i][j] = True
            continue        
        
        if c_p == '*':
            if match[i][j-2]:
                match[i][j] = True
                continue
            c_pp = p[j-2]
            c_match = (c_pp == '.') or (c_s == c_pp);
            if c_match and match[i-1][j]:
                match[i][j] = True
                continue
            
print(match[-1][-1])
                
        
        
        
        
        
        