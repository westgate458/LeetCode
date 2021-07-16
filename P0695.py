class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        def DFS(i, j):            
            grid[i][j] = 0            
            return sum([DFS(ii,jj) for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0 <= ii < r and 0 <= jj < c and grid[ii][jj]])+1        
        r, c = len(grid), len(grid[0])        
        return max([0]+[DFS(i, j) for i in range(r) for j in range(c) if grid[i][j]])