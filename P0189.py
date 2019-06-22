# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:15:55 2019

@author: Tianqi Guo
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """        
        # length of list
        l = len(nums)
        # no need to do more rotation than length of list
        k %= l        
        # swap elements in-place, put last k elements at the beginning
        nums[:k], nums[k:] = nums[-k:], nums[:l-k]
        
        # return nums
        
nums =  [1,2,3,4,5,6,7] 
k = 3

test = Solution()
print test.rotate(nums, k)