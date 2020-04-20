# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:22:15 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Solution 1 beats 94.70%: by iteration
        dp = set()
        for num in nums:
            for r in dp.copy():
                if num >= r[-1]: dp.add(r+(num,))
            dp.add((num,))
        return [r for r in dp if len(r)>1]
    
        # Solution 2 beats 40.40%: by recursion
        nums = [-101] + nums
        l = len(nums)
        self.dp = {}
        def DFS(p):
            if p not in self.dp:               
                self.dp[p] = set([(nums[p],)])
                for pp in range(p+1, l):
                    if nums[pp] >= nums[p]:
                        for r in DFS(pp):                            
                            self.dp[p].add((nums[p],)+r)
            return self.dp[p]       
        return [r[1:] for r in DFS(0) if len(r)>2]