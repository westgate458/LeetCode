# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:40:34 2019

@author: Tianqi Guo
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dictionary to record occurances
        d = {}
        # check each number
        for num in nums:
            # if it has not occured before
            if num not in d:
                # mark the dictionary
                d[num] = 1
            # if it has occured, then it is not we are looking for
            else:
                # remove it from dictionary
                del d[num]
        # all remaining keys are the numbers
        # that only appeared once
        return d.keys()