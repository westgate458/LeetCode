# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:24:01 2018

@author: Tianqi Guo
"""

s = "cbbd"
l = len(s)
m = 1
p = 0

TF = [[False] * l for i in range(l)]
for i in range(l):
    TF[i][i] = True
    
for i in range(l-1):
    TF[i][i+1] = (s[i] == s[i+1])
    if TF[i][i+1]:
        m = 2
        p = i
    
for m_ij in range(3,l + 1):    
    for i in range(0,l - m_ij + 1):
        j = i + m_ij - 1
        TF[i][j] = (s[i] == s[j]) and TF[i+1][j-1]      
        if TF[i][j]:
            m_ij = j - i + 1
            if m_ij > m:
                m = m_ij
                p = i               

print(s[p:p+m])
        
        
        