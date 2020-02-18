# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:19:49 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1 beats 99.83%: mark all visited with extra space
        visited = [0]*len(nums)
        res = []
        for num in nums:
            if visited[num-1]:
                res.append(num)
            else:
                visited[num-1] = 1
        return res
    
        # Solution 2 beats 48.74%: find solution in-place
        # deal with each position in the array
        # ideally we want num[p] = p at each position after loop
        for p in xrange(len(nums)):
            # keep switching array elements, until one of the two occurs:
            # 1) num[p] = p, 2) number at target position is the same as current position
            while nums[nums[p]-1] != nums[p]:
                nums[nums[p]-1], nums[p] = nums[p], nums[nums[p]-1]    
        # finally missing numbers will be filled with the numbers that appear twice
        return([num for p, num in enumerate(nums) if num - 1 != p])