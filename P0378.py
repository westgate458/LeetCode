# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:04:48 2019

@author: Tianqi Guo
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # Solution 1 beats 99.56%: binary search
        l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)        
        while l < r:             
            m, i, j, c = (l+r)//2, n-1, 0, 0            
            while i >= 0 and j < n:                
                if matrix[i][j] <= m:
                    c += i+1
                    j += 1                    
                else:
                    i -= 1 
            if c < k:
                l = m + 1
            else:
                r = m
        return l
        
        # Solution 2 beats 74.40%: 1-liner
        return sorted(n for a in matrix for n in a)[k-1]