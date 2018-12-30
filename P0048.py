# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:07:08 2018

@author: Tianqi Guo
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # size of the matrix
        s = len(matrix) - 1

        # depends on the size is even or odd
        # determine how many rows and columns need to be switched
        i_max = len(matrix)/2
        # in case of odd size, one more row need to be switched
        j_max = i_max + len(matrix)%2
        
        # for each element in the top-left quadrant
        for i in range(i_max):            
            for j in range(j_max):
                # clockwise switch the four elements in each quadrant 
                matrix[i][j],  matrix[j][s-i], matrix[s-i][s-j], matrix[s-j][i] = \
                matrix[s-j][i], matrix[i][j],  matrix[j][s-i], matrix[s-i][s-j]
        
        # no need to return since rotation is done in-place
        # return matrix

matrix = [ [1,2,3],
  [4,5,6],
  [7,8,9]  ]

test = Solution()
test.rotate(matrix)
print(matrix)
        
        
        
        