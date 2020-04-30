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
        # sum of all numbers
        sum_total = sum(nums)        
        # question is to split nums into two subsets S1 and S2
        # such that S1 - S2 = S,
        # with S1 + S2 = sum_total
        # we have S1 = (S + sum_total)//2 is integer
        # first deal with trivial cases where S1 is not possible
        if sum_total < S or (S + sum_total)%2: return 0        
        # target sum is S1        
        target = (S + sum_total)/2 
        # then question is for each number in nums, whether to include in S1
        # -> 0/1 backpack
        # dp[i][j] for the 0~i-th number, how many ways to get sum j
        dp = [1] + [0]*target      
        # then for i-th number, the number of ways is the sum of the two
        # 1) to use this number, then previously we have dp[i-1][j-nums[i]]
        # 2) to skip this number, then previously we have dp[i-1][j]
        # try each number one by one
        for n in nums:            
            # iterate over j, which is at most target, at least nums[i]
            for s in range(target,n-1,-1):
                # accumulate all ways
                dp[s] += dp[s-n]     
        # dp[-1] is not dp[len(nums)][target]
        return(dp[-1])