# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:15:19 2019

@author: Tianqi Guo
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # duplicate exists when element count is smaller for unique set
        return len(set(nums)) < len(nums)