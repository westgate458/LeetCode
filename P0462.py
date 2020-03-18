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
        # find the median after sorting
        median = sorted(nums)[len(nums)//2] 
        # min number of moves is by bringing each number to the median value
        return(sum([abs(num-median) for num in nums]))