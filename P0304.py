# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:51:26 2019

@author: Tianqi Guo
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # deal with trivial case
        if not matrix or not matrix[0]:
            return None         
        # size of the matrix           
        m, n = len(matrix), len(matrix[0])
        # accumulative sum
        self.temp = [[0] * (n+1) for _ in xrange(m+1)]        
        # calculate the accumulative, self.temp[i][j] contains sum of numbers from [0][0] to [i-1][j-1]
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                self.temp[i][j] = self.temp[i-1][j] + self.temp[i][j-1] - self.temp[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """        
        # get sum of the range from Venn diagram
        return self.temp[row2+1][col2+1] - self.temp[row1][col2+1] - self.temp[row2+1][col1] + self.temp[row1][col1]