class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:        
        s1, s2 = len(grid), len(grid[0])        
        n_keys = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '@':
                    m, n = i, j
                elif cell.islower():
                    n_keys += 1                
        seen = set([(m,n,'')])        
        q = [(m,n,'',0)]   
        for i,j,key,step in q:            
            for ii, jj in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if (0<=ii<s1) and (0<=jj<s2) and (grid[ii][jj]!='#'):  
                    keys_new = key
                    if grid[ii][jj].islower():                        
                        if grid[ii][jj] not in keys_new:
                            keys_new += grid[ii][jj]                        
                        if len(keys_new) == n_keys:
                            return step+1
                    elif grid[ii][jj].isupper() and (grid[ii][jj].lower() not in key):
                        continue                                       
                    if (ii,jj,keys_new) in seen: continue
                    seen.add((ii,jj,keys_new))
                    q.append((ii,jj,keys_new,step+1))         
        return(-1)