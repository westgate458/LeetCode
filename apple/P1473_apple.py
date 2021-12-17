class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        
        dp = [[[float('inf')] * target for _ in range(n)] for _ in range(m)]       
        
        if houses[0]==0:
            for j in range(n):
                dp[0][j][0] = cost[0][j]
        else:
            dp[0][houses[0]-1][0] = 0        
        
        for i in range(1,m):
            if houses[i]==0:
                for j in range(n):
                    for jj in range(n):
                        if j==jj:
                            for k in range(target):
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][jj][k] + cost[i][j])
                        else:                            
                            for k in range(1,target):
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][jj][k-1] + cost[i][j])                            
            else:
                for jj in range(n):
                    if jj==houses[i]-1:
                        for k in range(target):
                            dp[i][houses[i]-1][k] = min(dp[i][houses[i]-1][k], dp[i-1][jj][k])
                    else:
                        for k in range(1,target):
                            dp[i][houses[i]-1][k] = min(dp[i][houses[i]-1][k], dp[i-1][jj][k-1])
       
        res = min([dp[-1][j][-1] for j in range(n)])
        return -1 if res == float('inf') else res