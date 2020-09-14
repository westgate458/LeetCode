class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
		# 0-D DP + post processing
        if num == 1: return 2
        n2 = bin(num)[2:]
        dp = [1, 2] + [0] * (len(n2)-2)
        for i in range(2,len(n2)):
            dp[i] = dp[i-1]+dp[i-2]           
        dp, res, cc = dp[::-1], 0, '0'         
        for i, c in enumerate(n2):
            if c == '1':
                res += dp[i]
                if cc == '1':
                    return res            
            cc = c            
        return(res+1)

    