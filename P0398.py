# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:20:32 2019

@author: Tianqi Guo
"""

from random import choice
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # simply record the numbers
        self.nums = nums        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # first gather all the indices for this number
        # and then randomly choose one from them
        return choice([i for i, num in enumerate(self.nums) if num == target])        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)