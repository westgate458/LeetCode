# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:31:14 2020

@author: westg
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """       
        res = 0
        for r, row in enumerate(grid):
            for c, g in enumerate(row):
                if g == 1:                         
                    res += 4
                    if r > 0 and grid[r-1][c] == 1: res -= 2
                    if c > 0 and grid[r][c-1] == 1: res -= 2                    
        return res