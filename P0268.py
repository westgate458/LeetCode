# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:34:48 2019

@author: Tianqi Guo
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        
        # Solution 1 beats 98.03%: length and sum
        # length of the number list
        n = len(nums)       
        # calculate the difference between the expected sum and actual sum
        # which is the missing number
        return n * (n + 1)/2 - sum(nums)
    
        # Solution 2 beats 80.61%: min, max, sum
        a, b, s = max(nums), min(nums), sum(nums)
        d = (0 + a) * (a + 1)/2 - s        
        if b != 0:
            return 0
        elif d == 0:
            return a + 1
        else:
            return d