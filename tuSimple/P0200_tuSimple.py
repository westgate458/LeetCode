class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        res, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    q = [(i,j)]
                    grid[i][j] = -res
                    while q:
                        x, y = q.pop()
                        for xx, yy in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                            if (0<=xx<m) and (0<=yy<n) and (grid[xx][yy]=="1"):
                                q.append((xx,yy))
                                grid[xx][yy] = -res        
        return(res)