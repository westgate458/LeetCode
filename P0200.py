# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:36:03 2019

@author: Tianqi Guo
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # deal with trivial cases
        if not grid or not grid[0]:
            return 0
        # size of the grid
        r, c = len(grid), len(grid[0])        
        # indices for 4-connected neighborhood
        dd = [(0, -1), (0, 1), (1, 0), (-1, 0)];  
        # pad grid to deal with boundaries
        grid = [['0'] * (c+2)] + [['0'] + row + ['0'] for row in grid] + [['0'] * (c+2)]        
        # number of islands
        ans = 0
        # check each point in the grid
        for m in range(1,r+1):
            for n in range(1,c+1):
                # if this point has not been visited, a new island is discovered
                if grid[m][n] == '1':                    
                    # start flood-fill from this point
                    s = [(m,n)]
                    # mark visited point as 0
                    grid[m][n] = '0'         
                    # update the number of islands
                    ans += 1                    
                    # continue flood-fill while there are still points to check
                    while (s):                        
                        # current point
                        x, y = s.pop() 
                        # look around its neighborhood
                        for i in xrange(4):           
                            # coordinates of its neighborhood
                            xx, yy = x + dd[i][0], y + dd[i][1] 
                            # check if this neighborhood has been visited
                            if grid[xx][yy] == '1':                      
                                # add this point to the flood-fill stack
                                s.append((xx,yy))
                                # mark visted point with 0
                                grid[xx][yy] = '0'        
        # return number of islands
        return ans
    
grid = [['1','1','1','1','0'], ['1','1','0','1','0'],[ '1','1','0','0','0'], ['0','0','0','0','0']]

test = Solution()
print test.numIslands(grid)