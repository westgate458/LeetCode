# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:03:42 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        i = j = d = 0
        m, n = len(matrix), len(matrix[0])
        res = [0]*(m*n)        
        for idx in range(m*n):
            res[idx] = matrix[i][j]
            if d == 0: 
                if j == n-1:
                    i += 1                    
                    d = 1
                elif i == 0:
                    j += 1
                    d = 1                
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1                    
                    d = 0
                elif j == 0:
                    i += 1
                    d = 0                
                else:
                    i += 1
                    j -= 1
        return res
        