# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:04:49 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        p1, p2 = nums[0], nums[nums[0]]
        while p1 != p2:
            p1, p2 = nums[p1], nums[nums[p2]]            
        p1 = 0
        while p1 != p2:
            p1, p2 = nums[p1], nums[p2]
        return p1
        