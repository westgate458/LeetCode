class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])            
        dp = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: continue
                dp[i][j] = dp[i][j-1] + 1 if j else 1                   
                ones = dp[i][j]
                for k in range(min(dp[i][j],i+1)):
                    ones = min(ones, dp[i-k][j])
                    if ones >= k+1: res += 1
                    else: break 
        return res