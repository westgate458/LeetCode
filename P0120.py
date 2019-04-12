# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:36:52 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """  
        
        # obtain path from bottom up
        for i in range(len(triangle)-2,-1,-1):
            # for each element in current row, choose the path from row below
            for j in range(i+1):                
                # the path with lower sum
                # should come from the element on next row with smaller value
                # choose from two adjacent values, and add to current element
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])       
        
        # now the top element should be the minimum sum overall
        return triangle[0][0]
       

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]        
test = Solution()
print test.minimumTotal(triangle)