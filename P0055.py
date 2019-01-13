# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:12:37 2019

@author: Tianqi Guo
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)

        max_i = 0

        for i in range(l-1):

            if max_i < i:
                break

            if i + nums[i] > max_i:
                max_i = i + nums[i]

        if max_i >= l-1:
            return True
        else:
            return False
        

nums = [3,2,1,0,4]
test = Solution()
print(test.canJump(nums))