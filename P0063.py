# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:40:09 2019

@author: Tianqi Guo
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        # size of the grid
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        # initialize the states for each column
        steps = [0] * (m+1)
        # steps at 0 is set to be 0 as the boundary
        # steps at 1 corresponds to the 1st column
        steps[1] = 1
        
        # determine the states from ↖ towards ↘
        for i in range(n):
            # the boundary value at steps[0] is not updated
            for j in range(1,m+1):
                # if there is an obstacle at (i, j-1)
                if obstacleGrid[i][j-1]:
                    # set the states (number of paths via current grid) to zero
                    steps[j] = 0
                # if there is no obstacle
                else:
                    # update the states (number of paths via current grid)
                    # as the sum of states from top (same column) and left (previous column)
                    steps[j] = steps[j] + steps[j-1]
        
        # return the total number of paths at finish point
        return steps[-1]    


obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]]

test = Solution()
print test.uniquePathsWithObstacles(obstacleGrid)