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
        n = len(grid)
        m = len(grid[0])

        num_inf = float('inf')

        grid = [[num_inf] + x for x in grid]
        grid = [[num_inf] * (m+1)] + grid
        grid[1][0] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if grid[i-1][j] < grid[i][j-1]:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + grid[i][j-1]

        return grid[-1][-1]
    

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
test = Solution()
print(test.minPathSum(grid))