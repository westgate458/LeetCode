# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:46:45 2020

@author: Tianqi Guo
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """       
        # Solution 1 beats 100%: sort + DFS
        total_sum = sum(nums)
        nums.sort(reverse=True)
        if total_sum%2 != 0:
            return False
        def DFS(target, nums):
            for p, num in enumerate(nums):                
                if num > target:
                    return False
                elif num == target:
                    return True
                elif DFS(target-num, nums[p+1:]):
                    return True
        return DFS(total_sum//2, nums)
    
        # Solution 2 beats 25.64%: naive DP
        l, total_sum = len(nums), sum(nums)                
        if total_sum%2 != 0:
            return False                
        dp = [[False] * (l+1)  for _ in xrange(total_sum+1)]        
        for idx, num in enumerate(nums):
            dp[num][idx+1] = True        
        for i in xrange(total_sum//2):
            for j in xrange(l):                
                if dp[i][j]:
                    dp[i+nums[j]][j+1] = True
                    dp[i][j+1] = True
        return(sum(dp[total_sum//2])>0)