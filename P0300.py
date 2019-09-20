# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:07:53 2019

@author: Tianqi Guo
"""
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1 beats 98.22%: dynamic programing + binary search        
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
        
        # Solution 2 beats 62.61%: dynamic programing
        if not nums:
            return 0
        ls = [1] * len(nums)
        for i, n1 in enumerate(nums):            
            for j, n2 in enumerate(nums[:i]):
                if n2 < n1 and ls[j] + 1 > ls[i]:
                    ls[i] = ls[j] + 1           
        return max(ls)
                
                
        