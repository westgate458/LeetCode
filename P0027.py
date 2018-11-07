# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:28:40 2018

@author: Tianqi Guo
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        while p < len(nums):
            if nums[p] == val:
                nums.pop(p)
            else:
                p = p + 1                
        return len(nums)
        
nums = [0,1,2,2,3,0,4,2]
val = 2      
test = Solution()
p = test.removeElement(nums, val)
print(p) 