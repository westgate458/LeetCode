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
        # deal with each position in the array
        # ideally we want num[p] = p at each position after loop
        for p in xrange(len(nums)):
            # keep switching array elements, until one of the two occurs:
            # 1) num[p] = p, 2) number at target position is the same as current position
            while nums[nums[p]-1] != nums[p]:
                nums[nums[p]-1], nums[p] = nums[p], nums[nums[p]-1]    
        # finally missing numbers will be filled with the numbers that appear twice
        return([p+1 for p, num in enumerate(nums) if num - 1 != p])