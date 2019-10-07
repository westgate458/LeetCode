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
        # pad array with virtual balloons
        nums = [1] + nums + [1]
        # number of balloons
        l = len(nums)
        # initialize dp array by 0 coin earned
        # dp[i][j] is the max coins earned in the range [i, j]
        dp = [[0] * l for _ in xrange(l)]   
        # construct longer dp span from shorter spans
        # start span from length 1, i.e. individual balloons
        for ll in xrange(1, l+1):
            # i: start point of the range
            for i in xrange(1, l-ll):
                # j: end point of the range
                j = i + ll - 1
                # try each balloon in the range as the last one to burst
                for k in xrange(i,j+1):
                    # calculate the coins earned if we burst this balloon as the last one
                    # i.e. we have already earned coins in the range [i, k-1], and range [k+1,j]
                    # plus the coins for the last bursting is from k-th balloon and the ones left beside it
                    coins = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    # update dp for current range
                    if coins > dp[i][j]:
                        dp[i][j] = coins      
        # the coins earned for the original range
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