# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:22:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                nums[i-zeros] = num
        if zeros > 0:
            nums[-zeros:] = [0] * zeros