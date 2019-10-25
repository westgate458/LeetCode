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
        # current smallest and 2nd smallest found
        # if later numbers are smaller, we update accordingly
        m = n = float('inf')
        # check each number
        for num in nums:
            # update smallest
            if num <= m:
                m = num
            # update 2nd smallest
            elif num <= n:
                n = num
            # if current is larger than both found
            else:
                # then we got an increasing triplet
                return True
        # if after all numbers are checked, no 3rd number is found
        # no increasing triplet in the list
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