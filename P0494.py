# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:03:52 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_total = sum(nums)        
        if sum_total < S or (S + sum_total)%2:
            return 0        
        target = (S + sum_total)/2 
        dp = [1] + [0]*target      
        for n in nums:            
            for s in range(target,n-1,-1):
                dp[s] += dp[s-n]     
        return(dp[-1])