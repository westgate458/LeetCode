# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:37:21 2018

@author: Tianqi Guo
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = len(nums)  
        
        if l == 0:
            return 0
        
        h = 0
        t = l - 1
        
        while h <= t:
            
            m = h + (t - h)/2
            
            if nums[m] == target:
                return m
            
            if nums[m] < target:
                h = m + 1
                
            if nums[m] > target:
                t = m - 1
        
        return h

nums = [1,3]
target = 0

test = Solution()
print(test.searchInsert(nums,target))