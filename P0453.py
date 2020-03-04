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
        # steps for making all numbers equal
        # 1) pick the smallest number i
        # 2) pick the current largest number j
        # 3) make m_ji = (nums[j]-nums[i]) moves for all other numbers except j, now i, j are equal
        # 4) repeat 2) and 3) until all numbers are equal
        # so in total the number of moves are the sum of all m_ji
        # i.e. the sum of difference between all numbers and the smallest number 
        # res = sum(nums[j]-nums_min) for all j
        return sum(nums)-min(nums)*len(nums)