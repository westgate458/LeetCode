# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:09:42 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # size of the grid
        n = len(grid)
        m = len(grid[0])
        
        # maximum number to put on the boundary
        num_inf = float('inf')
        
        # place boundary numbers on the left and top
        # to avoid conditional statements in the loops
        grid = [[num_inf] + x for x in grid]
        grid = [[num_inf] * (m+1)] + grid
        grid[1][0] = 0
        
        # determine the states (minimum sum) from ↖ towards ↘
        for i in range(1,n+1):
            for j in range(1,m+1):
                # determine the path with smaller sum between top and left
                # and update the state of current grid
                if grid[i-1][j] < grid[i][j-1]:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
        
        # return the minimum sum at the finish point
        return grid[-1][-1]
    

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
test = Solution()
print(test.minPathSum(grid))