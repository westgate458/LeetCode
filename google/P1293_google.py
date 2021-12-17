class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Solution 1: backwards
        m, n = len(grid), len(grid[0])
        q = [(m-1,n-1,k)]    
        res = [[float('inf')] * n for _ in range(m)]        
        res[m-1][n-1] = 0
        for x, y, r in q:
            bs_0, bs_1 = [], []            
            for xx, yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=xx<m and 0<=yy<n and res[xx][yy] > res[x][y]+1:
                    if grid[xx][yy] == 0: bs_0.append((xx,yy))
                    elif r>0 and grid[xx][yy] == 1: bs_1.append((xx,yy))                        
            for xx, yy in bs_0:
                q.append((xx,yy,r))
                res[xx][yy] = res[x][y]+1            
            for xx, yy in bs_1:
                q.append((xx,yy,r-1))
                res[xx][yy] = res[x][y]+1                            
        return res[0][0] if res[0][0]<float('inf') else -1
        
        # Solution 2: forwards        
        m, n = len(grid), len(grid[0])
        q = [(0,0,0,0)]   
        dp = [[float('inf')] * n for _ in range(m)]       
        for x, y, c, o in q:            
            if o >= dp[x][y]: continue
            if x == m-1 and y == n-1: return c
            dp[x][y] = o
            if grid[x][y]: o += 1
            if o > k: continue
            for xx, yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=xx<m and 0<=yy<n:
                    q.append((xx,yy,c+1,o))                           
        return -1