class Solution(object):    
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """    
		# 2D DP with conditional paths
        dp = [[0] * (k + 1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(k+1):     
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - (0 if j < i else dp[i-1][j-i])                     
        return dp[n][k]%1000000007