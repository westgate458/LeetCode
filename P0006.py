# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:41:45 2018

@author: Tianqi Guo
"""

s = "PAYPALISHIRING"
numRows = 4

zigzag = [[] for i in range(numRows)]
row_num = -1
direction = 0

for i in range(len(s)):
    if direction == 0:
        if row_num < numRows - 1:
            row_num = row_num + 1            
        else:
            direction = 1
            row_num = row_num - 1
    else:
        if row_num > 0:
            row_num = row_num - 1            
        else:
            direction = 0
            row_num = row_num + 1 
    zigzag[row_num].append(s[i])

ans = ''
for i in range(numRows):
    for j in range(len(zigzag[i])):
        ans = ans + zigzag[i][j]

return ans
        
        
            
            
            
            
            
        

    
    