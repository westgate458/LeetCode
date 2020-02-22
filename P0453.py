# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:21:14 2020

@author: Tianqi Guo
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        return sum(nums)-min(nums)*len(nums)