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
        
        # length of the list
        l = len(nums)  
        # deal with trivial case
        if l == 0:
            return 0
        
        # initialize the endpoints for binary seaching
        h = 0
        t = l - 1
        # continue searching until endpoints meet
        while h <= t:
            # take the median
            m = h + (t - h)/2
            # if the median is the target
            if nums[m] == target:
                # return the position
                return m
            # if median is smaller than target            
            if nums[m] < target:
                # the target is in the 2nd half, update head
                h = m + 1
            # if median is larger than target                
            if nums[m] > target:
                # the target is in the 1st half, update tail
                t = m - 1
        
        # if target not already in the list        
        # since the searching ends when h > t
        # at this point, num[t] < target < num[h]
        # the target should be inserted at h
        return h

nums = [1,3]
target = 0

test = Solution()
print(test.searchInsert(nums,target))