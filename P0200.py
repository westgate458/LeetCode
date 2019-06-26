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
        
        if not grid or not grid[0]:
            return 0
        
        r, c = len(grid), len(grid[0])        
        dd = [(0, -1), (0, 1), (1, 0), (-1, 0)];  
        
        grid = [['0'] * (c+2)] + [['0'] + row + ['0'] for row in grid] + [['0'] * (c+2)]        
        ans = 0
        
        for m in range(1,r+1):
            for n in range(1,c+1):
                if grid[m][n] == '1':                    
                    s = [(m,n)]
                    grid[m][n] = '0'                    
                    ans += 1                    
                    while (s):                        
                        x, y = s.pop()                    
                        for i in xrange(4):                            
                            xx, yy = x + dd[i][0], y + dd[i][1] 
                            if grid[xx][yy] == '1':                                
                                s.append((xx,yy))
                                grid[xx][yy] = '0'        
        return ans
    
grid = [['1','1','1','1','0'], ['1','1','0','1','0'],[ '1','1','0','0','0'], ['0','0','0','0','0']]

test = Solution()
print test.numIslands(grid)