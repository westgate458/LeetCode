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
        # dp： increasing subseq upto this point
        dp = set()
        # chech each number
        for num in nums:
            # check previous subseq
            for r in dp.copy():
                # if current number is larger that the last in seq
                # extend the seq and add the new seq to dp
                if num >= r[-1]: dp.add(r+(num,))
            # add current number itself to dp
            dp.add((num,))
        # keep subseqs that have least 2 nums
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