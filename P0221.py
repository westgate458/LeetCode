# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:14:11 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # Similar to P0085
        # but we are looking for squares instead of rectangles
        
        # deal with trivial cases
        if not matrix or not matrix[0]:
            return 0
        
        # width of the matrix
        n = len(matrix[0])        
        
        # lengths of the continued 1's in each column up to current row
        areas = [0]* (n+1)
        # length of the side of the largest square
        l_max = 0
        # check each row
        for row in matrix:
            # update the lengths of the continued 1's in each column
            # previous length +1 if current column is 1
            # back to 0 if current column is 0
            areas = [areas[i] + 1 if row[i] == '1' else 0 for i in range(n)] + [0]             
            # indices of columns with non-decreasing lengths
            ps = [-1]            
            # check each column
            for p in range(n+1): 
                # for each previous column with larger lengths of 1's than current column
                while areas[p] < areas[ps[-1]]:
                    # get the previous length of 1's
                    pp = ps.pop()    
                    # update the max side length
                    # this part is different from P0085 in a way
                    # that we take the smaller value between width and height of the rectangle
                    l_max = max(l_max, min(p - ps[-1] - 1, areas[pp]))            
                # place current column index in to the non-decreasing-length list
                ps.append(p)
        
        # max area is the square of the max side length
        return l_max * l_max