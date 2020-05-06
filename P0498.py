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
        # trivial case
        if not matrix: return []
        # initial position, direction d=0 for upward move
        i = j = d = 0
        # size of the matrix
        m, n = len(matrix), len(matrix[0])
        # final path
        res = [0]*(m*n)        
        # deal with each point
        for idx in range(m*n):
            # record value
            res[idx] = matrix[i][j]
            # deal with upward move
            if d == 0: 
                # if at right edge
                if j == n-1:
                    # move to the one below and change direction
                    i += 1                    
                    d = 1
                # if at top edge
                elif i == 0:
                    # move to the one on the right and change direction
                    j += 1
                    d = 1                
                # for interior points, continue moving along the direction
                else:
                    i -= 1
                    j += 1
            # similarly, deal with downward move
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
        # return the values along the path
        return res
        