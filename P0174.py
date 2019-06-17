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
        # size of the board
        s1, s2 = len(dungeon), len(dungeon[0])             
        # s[i][j] is the minimum health required at this point in order to proceed till the end
        # initialize state function with inf so any smaller number would be updated
        # set last state to 1, so at least 1 HP is required
        # pad state function with one more inf to deal with boundary
        s = [float('inf')] * (s2 - 1) + [1] + [float('inf')] 
        # start from the last cell, proceed backwards
        for i in range(s1)[::-1]:           
            # update each state from right to left
            for j in range(s2)[::-1]:             
                # current state is to choose from the smaller requirement
                # between the cell below and the cell on the right
                # also if current cell has magic orb, and its value is larger than required HP till end
                # we only need to reach current cell with 1 HP, take the orb and go on
                s[j] = max(min(s[j],s[j+1]) - dungeon[i][j],1)    
        # first state is the required HP to start with so we can proceed till end
        return s[0]

dungeon = [[-2,  -3,  3],
           [-5, -10,  1],
           [10,  30, -5]]      
test = Solution()
print test.calculateMinimumHP(dungeon)