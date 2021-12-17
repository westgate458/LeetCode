class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        m, n = len(grid), len(grid[0])        
        dp_0 = [[0] * n for _ in range(n)]
        dp_1 = [[0] * n for _ in range(n)] 
        for i in range(1,m):
            for j in range(min(i+1,n-1)):
                for k in range(max(j,n-i-1),n):
                    candidates = []
                    for dj in [-1,0,1]:
                        for dk in [-1,0,1]:
                            jj = j + dj
                            kk = k + dk
                            if 0<=jj<n and 0<=kk<n:
                                candidates += [dp_0[jj][kk]]
                    dp_1[j][k] = max(candidates) + grid[i][j] + grid[i][k]
                    if j==k: dp_1[j][k] -= grid[i][k]
            dp_0 = dp_1
            dp_1 = [[0] * n for _ in range(n)]              
        return(max([max(r) for r in dp_0])+grid[0][0]+grid[0][-1])
        