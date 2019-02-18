# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:27:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        
        for num in nums:
            if l < 2 or nums[l-2] < num:
                nums[l] = num
                l += 1
                            
        return l
        
nums = [1,1,1,2,2,3]
test = Solution()
print test.removeDuplicates(nums)