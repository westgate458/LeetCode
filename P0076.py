# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 22:35:02 2019

@author: Tianqi Guo
"""

s = "ADOBECODEBANC"
t = "ABC"

n = len(t)
ss = ''
m_l = float('inf')   

count = {}
        
for i in range(n):
    if not t[i] in count:
        count[t[i]] = 1
    else:
        count[t[i]] = count[t[i]] + 1   

p0 = 0

for i in range(len(s)):
    
    if s[i] in t:  
        
        count[s[i]] = count[s[i]] - 1
        
        if count[s[i]] >= 0:
            n = n - 1
        
        while (not (s[p0] in t)) or (count[s[p0]] + 1 <= 0):            
            if s[p0] in t:
                count[s[p0]] = count[s[p0]] + 1
            p0 = p0 + 1
        
        if (n == 0) and (i - p0 + 1 < m_l):
            ss = s[p0:i+1]
            m_l = i - p0 + 1 
           
            
            
        
        
        
    