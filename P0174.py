# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:39:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """      
        s1, s2 = len(dungeon), len(dungeon[0])     
        s = [float('inf')] * (s2 - 1) + [1] + [float('inf')] 
        for i in range(s1)[::-1]:           
            for j in range(s2)[::-1]:                
                s[j] = max(min(s[j],s[j+1]) - dungeon[i][j],1)        
        return s[0]

dungeon = [[-2,  -3,  3],
           [-5, -10,  1],
           [10,  30, -5]]      
test = Solution()
print test.calculateMinimumHP(dungeon)