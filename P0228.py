# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:59:13 2019

@author: Tianqi Guo
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        start = nums[0]
        p = 1
        nums += [float('inf')]
        while p < len(nums):            
            if nums[p-1] + 1 != nums[p]:
                res.append(str(start))
                if nums[p-1] != start:
                    res[-1] += '->'+str(nums[p-1])
                start = nums[p]            
            p += 1                
        return res