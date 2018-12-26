# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:07:08 2018

@author: Tianqi Guo
"""




matrix = [ [1,2,3],
  [4,5,6],
  [7,8,9]  ]


s = len(matrix) - 1

i_max = len(matrix)/2
j_max = i_max + len(matrix)%2

for i in range(i_max):
    for j in range(j_max):
        matrix[i][j],  matrix[j][s-i], matrix[s-i][s-j], matrix[s-j][i] = \
        matrix[s-j][i], matrix[i][j],  matrix[j][s-i], matrix[s-i][s-j]

print(matrix)
        
        
        
        