class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n, res = len(grid), len(grid[0]), 0
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    q = [(i,j)]
                    grid[i][j] = '0'
                    for x, y in q:
                        for xx, yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if 0<=xx<m and 0<=yy<n and grid[xx][yy]=='1':
                                grid[xx][yy] = '0'
                                q.append((xx,yy))
        return res
                    
                
       
       
       