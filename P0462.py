# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 00:32:23 2020

@author: Tianqi Guo
"""

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """          
        median = sorted(nums)[len(nums)//2] 
        return(sum([abs(num-median) for num in nums]))