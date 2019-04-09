# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:37:56 2019

@author: Tianqi Guo
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        
        pascal = [[1]]
        for _ in range(numRows-1):
            pascal.append([a + b for (a, b) in zip(pascal[-1] + [0], [0] + pascal[-1])])
        
        return pascal
    
test = Solution()
print test.generate(5)