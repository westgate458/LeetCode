class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.dp = {}
        def DFS(i, j, s):            
            if s == 0: return 1
            if (i,j,s) not in self.dp:                
                self.dp[(i,j,s)] = 0
                for ii, jj in [(i-2,j-1),(i-1,j-2),(i+2,j-1),(i+1,j-2),(i-2,j+1),(i-1,j+2),(i+2,j+1),(i+1,j+2)]:
                    if (0<=ii<n) and (0<=jj<n):
                        self.dp[(i,j,s)] += DFS(ii,jj,s-1)                
            return self.dp[(i,j,s)]
        return DFS(row, column, k)/(8**k)
                
        