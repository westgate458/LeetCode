class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)       
        q = []
        for i in range(m):
            for j in range(m):
                if grid[i][j] == 1:
                    q = [(i,j)]
                    grid[i][j] = [-1]
                    break
            if q:
                break
                        
        qq = set()
        while q:
            i, j = q.pop()
            for ii, jj in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                if 0 <= ii < m and 0 <= jj < m:
                    if grid[ii][jj] == 1:
                        q.append((ii,jj))
                        grid[ii][jj] = -1
                    elif grid[ii][jj] == 0 and (i,j,0) not in qq:
                        qq.add((i,j,0))
                        
        qq = list(qq)        
        for i, j, s in qq:           
            for ii, jj in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                if 0 <= ii < m and 0 <= jj < m:
                    if grid[ii][jj] == 1:
                        return(s)
                    elif grid[ii][jj] == 0:
                        qq.append((ii,jj,s+1))
                        grid[ii][jj] = -1