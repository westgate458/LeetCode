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
        # Solution 1 beats 99.58%: move to front directly
        j = 0
        for i, num in enumerate(nums):
            if num != 0: nums[j], j = num, j+1
        nums[j:] = [0] * (len(nums)-j)
        
        # Solution 2 beats 89.83%: move to back first
        # how many zeros before current number
        zeros = 0
        # check each number
        for i, num in enumerate(nums):
            # if current number is 0
            if num == 0:
                # update counter
                zeros += 1
            # if current number is not 0
            else:
                # move it to last non-zero position
                nums[i-zeros] = num
        # if we have zeros to move
        if zeros > 0:
            # fill the last of nums with 0's
            nums[-zeros:] = [0] * zeros