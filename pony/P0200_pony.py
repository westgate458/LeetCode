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
                    grid[i][j] = '0'
                    q = [(i,j)]
                    for ii, jj in q:
                        for x, y in [(ii-1, jj),(ii+1, jj),(ii, jj-1),(ii, jj+1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                grid[x][y] = '0'
                                q.append((x,y))
        return res
                                
                        
                    