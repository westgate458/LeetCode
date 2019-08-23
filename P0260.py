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
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                del d[num]
        return d.keys()