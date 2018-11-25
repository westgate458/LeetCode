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
        
        # start traverse from head
        p = 0
        # for each element compare with target value
        while p < len(nums):
            # if target value found
            if nums[p] == val:
                # remove this element
                nums.pop(p)
            else:
                # if not found continue searching
                p = p + 1                
                
        # return list length after removal of elements
        return len(nums)
        
nums = [0,1,2,2,3,0,4,2]
val = 2      
test = Solution()
p = test.removeElement(nums, val)
print(p) 