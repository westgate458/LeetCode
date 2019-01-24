# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:40:09 2019

@author: Tianqi Guo
"""

obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]]

n = len(obstacleGrid)
m = len(obstacleGrid[0])

steps = [0] * (m+1)
steps[1] = 1

for i in range(n):
    for j in range(1,m+1):
        if obstacleGrid[i][j-1]:
            steps[j] = 0
        else:
            steps[j] = steps[j] + steps[j-1]

print steps[-1]        
            