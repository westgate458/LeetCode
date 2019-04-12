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
        
        # deal with trivial case
        if numRows == 0:
            return []
        
        # start with the first level
        pascal = [[1]]
        # calculate next levels
        for _ in range(numRows-1):
            # entries on next level obtained from 
            # adding adjacent values together on current level
            pascal.append([a + b for (a, b) in zip(pascal[-1] + [0], [0] + pascal[-1])])
        
        # return the pascal triangle
        return pascal
    
test = Solution()
print test.generate(5)