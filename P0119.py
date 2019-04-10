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
        
        pascal = [1 for x in range(rowIndex+1)]
        
        for i in range(1,(rowIndex)//2+1):          
            pascal[i] = pascal[i-1] * (rowIndex - i + 1)/ i
            pascal[rowIndex - i] = pascal[i]

        return pascal
    
test = Solution()
print test.getRow(5)