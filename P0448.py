# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:49:56 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """  
        # Solution 1 beats 88.02%: using extra space
        return(set(range(1,len(nums)+1)) - set(nums))
        
        # Solution 2 beats 36.02%: find solution in-place
        for p in xrange(len(nums)):
            while nums[nums[p]-1] != nums[p]:
                nums[nums[p]-1], nums[p] = nums[p], nums[nums[p]-1]              
        return([p+1 for p, num in enumerate(nums) if num - 1 != p])