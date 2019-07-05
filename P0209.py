# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:01:57 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """        
        l, h, s_now = float('inf'), 0, 0        
        for t in xrange(len(nums)):
            s_now += nums[t]
            while s_now >= s:
                l = min(l, t - h + 1)
                s_now -= nums[h]
                h += 1
        return 0 if l == float('inf') else l 

s = 7
nums = [2,3,1,2,4,3]
test = Solution()
print test.minSubArrayLen(s, nums)
            