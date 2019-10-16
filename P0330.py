# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:39:00 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        range_upper, i, ans, l = 1, 0, 0, len(nums)
        while range_upper <= n:
            if i < l and nums[i] <= range_upper:
                range_upper += nums[i]
                i += 1
            else:                
                range_upper += range_upper
                ans += 1                
        return ans