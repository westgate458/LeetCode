# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:38:10 2019

@author: Tianqi Guo
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """                  
        
        # initialize the current row
        pascal = [1 for x in range(rowIndex+1)]
        
        # obtain the first half, and copy to second half
        for i in range(1,(rowIndex)//2+1):          
            # obtain next element on current row from current element
            # based on the combination formula
            pascal[i] = pascal[i-1] * (rowIndex - i + 1)/ i
            # copy to corresponding element in the second half
            pascal[rowIndex - i] = pascal[i]
        
        # return current row in pascal triangle
        return pascal
    
test = Solution()
print test.getRow(5)