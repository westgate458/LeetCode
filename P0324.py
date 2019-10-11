# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:50:05 2019

@author: Tianqi Guo
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """        
        n_s = sorted(nums, reverse = True)
        m = len(nums)//2
        nums[::2], nums[1::2] = n_s[m:], n_s[:m] 