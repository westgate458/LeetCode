class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        n_island = 0        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    n_island += 1
                    grid[i][j] = -n_island
                    q = [(i,j)]
                    for ii,jj in q:
                        for x, y in [(ii-1,jj),(ii+1,jj),(ii,jj-1),(ii,jj+1)]:
                            if 0<=x<m and 0<=y<n and grid[x][y]==1:
                                grid[x][y] = -n_island
                                q.append((x,y))
        
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==-1:
                    q.append((i,j,0))
                    
        for ii, jj, s in q:
            for x, y in [(ii-1,jj),(ii+1,jj),(ii,jj-1),(ii,jj+1)]:
                if 0<=x<m and 0<=y<n:
                    if grid[x][y]==-2:
                        return s
                    elif grid[x][y]==0:
                        grid[x][y] = -1
                        q.append((x,y,s+1))       
        
        return 0
                                
                            
                    