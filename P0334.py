# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:56:58 2019

@author: Tianqi Guo
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1 beats 67.12%: simplified version
        m = n = float('inf')
        for num in nums:
            if num <= m:
                m = num
            elif num <= n:
                n = num
            else:
                return True
        return False
        
#        # Solution 2 beats 38.61%: adaptation from P0300
#        dp = []
#        for num in nums:
#            idx = bisect.bisect_left(dp, num)
#            if idx == len(dp):
#                dp.append(num)
#            else:
#                dp[idx] = num
#            if len(dp) == 3:
#                return True
#        return False