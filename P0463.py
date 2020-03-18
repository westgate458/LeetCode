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
        # length of the perimeter
        res = 0
        # check each grid point
        for r, row in enumerate(grid):
            for c, g in enumerate(row):
                # if current grid point is land
                if g == 1:    
                    # first assume all four neighbors are water
                    res += 4
                    # if current grid point has ← and ↑ land neighbors
                    # then length of perimeter should decrease by 2 (mutually cancel out)
                    if r > 0 and grid[r-1][c] == 1: res -= 2
                    if c > 0 and grid[r][c-1] == 1: res -= 2                    
        return res