# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:40:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        max_num = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > max_num:
                    max_num = matrix[i][j]
        max_num = max_num + 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = max_num
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = max_num              

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == max_num:
                    matrix[i][j] = 0
                    
        return matrix

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]      

test = Solution()
print test.setZeroes(matrix)