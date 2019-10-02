# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:51:15 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        # Solution 1 beats 91.27%: iterative DP
        nums = [1] + nums + [1]
        l = len(nums)
        dp = [[0] * l for _ in xrange(l)]         
        for ll in xrange(1, l+1):
            for i in xrange(1, l-ll):
                j = i + ll - 1
                for k in xrange(i,j+1):
                    coins = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    if coins > dp[i][j]:
                        dp[i][j] = coins      
        return dp[1][l-2]
        
#        # Solution 2 beats 11.19%: recursive DP
#        def burst(i, j):      
#            if self.dp[i][j] == 0:                 
#                for k in range(i,j+1):
#                    self.dp[i][j] = max(self.dp[i][j], nums[i-1] * nums[k] * nums[j+1] + burst(i, k-1) + burst(k+1,j))         
#            return self.dp[i][j]
#        
#        nums = [1] + nums + [1]
#        l = len(nums)
#        self.dp = [[0] * l for _ in xrange(l)]   
#        return burst(1,l-2)

nums = [3, 1, 5, 8]        
test = Solution()
print(test.maxCoins(nums))