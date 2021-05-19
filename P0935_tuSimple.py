class Solution:
    def knightDialer(self, n: int) -> int:        
        dp = [1] * 10
        for _ in range(n-1):            
            dp = [(dp[4] + dp[6])%1000000007,
                  (dp[6] + dp[8])%1000000007,
                  (dp[7] + dp[9])%1000000007,
                  (dp[4] + dp[8])%1000000007,
                  (dp[0] + dp[3] + dp[9])%1000000007,
                  0,
                  (dp[0] + dp[1] + dp[7])%1000000007,
                  (dp[2] + dp[6])%1000000007,
                  (dp[1] + dp[3])%1000000007,
                  (dp[2] + dp[4])%1000000007                
            ]           
        return(sum(dp)%1000000007)
        
        