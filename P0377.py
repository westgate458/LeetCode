# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:17:49 2019

@author: Tianqi Guo
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        
        # Solution 1 beats 93.03%: DP
        # deal with trivial case
        if not nums:
            return 0        
        # dp for each number
        dp = [0] * (target+max(nums))
        # base case of number 0: # of combo is 1
        dp[0] = 1
        # for each number in the achievable range
        for n in xrange(target):
            # the next achievable number from current number
            for num in nums:
                # number of combos for next number
                # is the accumulative times when it has been accessed
                dp[n+num] += dp[n]       
        # number of combos for the target number
        return dp[target]
    
        # Solution 2 beats 93.03%: DFS + memorization
        nums.sort()       
        self.d = collections.defaultdict(int)
        self.d[0] = 1        
        def DFS(r):
            if r not in self.d:                
                for num in nums[0:bisect.bisect_right(nums, r)]:
                    self.d[r] += DFS(r-num)
            return self.d[r]    
        return DFS(target)