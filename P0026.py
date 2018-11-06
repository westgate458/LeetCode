# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:01:45 2018

@author: Tianqi Guo
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                
        p = 1
        while p < len(nums):
            if nums[p] != nums[p-1]:                
                p = p + 1               
            else:
                nums.pop(p)
            
        return len(nums)
        
        
nums = [1,1]
test = Solution()
p = test.removeDuplicates(nums)
print(p)