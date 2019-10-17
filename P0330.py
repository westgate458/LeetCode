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
        # range_upper: current achievable range is [0, range_upper)
        # i: index of current number
        # l: total numbers
        # ans: counter for added numbers
        range_upper, i, ans, l = 1, 0, 0, len(nums)
        # continue until we can achieve target
        while range_upper <= n:
            # if we have more numbers to use
            # and current number is within current range
            if i < l and nums[i] <= range_upper:
                # we can simply extend the range by adding current number
                range_upper += nums[i]
                # move on to next number
                i += 1
            # if we have used all numbers, or current number is beyond achievable range
            else:                
                # for current set of numbers, we can not achieve current upper limit
                # simply add the upper range number to the set of numbers
                # therefore the achievable range now is doubled
                range_upper += range_upper
                # update the counter
                ans += 1                
                # we do not update i, since we want to check if current number is still beyond achievable range
        return ans