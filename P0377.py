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
        if not nums:
            return 0        
        dp = [0] * (target+max(nums))
        dp[0] = 1
        for n in xrange(target):
            for num in nums:
                dp[n+num] += dp[n]       
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
                
    
        
            
