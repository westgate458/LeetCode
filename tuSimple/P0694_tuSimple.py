class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res, m, n = 0, len(grid), len(grid[0])
        islands = set()
        n_distinct = 0
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    res += 1
                    q = [(i,j,1)]
                    grid[i][j] = -res
                    island = 0
                    for x, y, t in q:    
                        island += t
                        for k, (xx, yy) in enumerate([(x+1,y),(x,y+1),(x-1,y),(x,y-1)]):
                            if (0<=xx<m) and (0<=yy<n) and (grid[xx][yy]==1):
                                if k == 0:
                                    q.append((xx,yy,t*10))
                                    grid[xx][yy] = -res        
                                elif k == 1:
                                    q.append((xx,yy,t+1))
                                    grid[xx][yy] = -res  
                                elif k == 2:
                                    q.append((xx,yy,t/10))
                                    grid[xx][yy] = -res  
                                elif k == 3:
                                    q.append((xx,yy,t/100))
                                    grid[xx][yy] = -res  
                                
                    if island not in islands:
                        n_distinct += 1
                        islands.add(island)                        
        
        return(n_distinct)