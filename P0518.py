class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """          
		# update coin in outer loop to avoid duplicate combinations
        dp = [1] + [0] * amount        
        for coin in coins: 
            for n in xrange(amount-coin+1):
                if dp[n]:
                    dp[coin+n] += dp[n]            
        return(dp[-1])
            