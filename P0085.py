# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:06:55 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0
              
        n = len(matrix[0])        
        
        areas = [0]* (n+1)
        area = 0

        for row in matrix:
            areas = [areas[i] + 1 if row[i] == '1' else 0 for i in range(n)] + [0]             
            ps = [-1]            
            for p in range(n+1):                
                while areas[p] < areas[ps[-1]]:
                    pp = ps.pop()            
                    area_pp = (p - ps[-1] - 1) * areas[pp]
                    if area_pp > area:
                        area = area_pp 
                ps.append(p)
       
        return area

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

test = Solution()
print test.maximalRectangle(matrix)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    