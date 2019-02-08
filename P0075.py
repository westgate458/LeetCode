# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:32:51 2019

@author: Tianqi Guo
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """        
        h = 0
        t = len(nums)-1
        p = 0
        
        while p <= t:       
            if nums[p] == 2:
                nums[p], nums[t] = nums[t], nums[p]        
                t = t - 1
            elif nums[p] == 0:
                nums[p], nums[h] = nums[h], nums[p]      
                h = h + 1
                p = p + 1
            else:
                p = p + 1
        return
    
nums = [2,0,2,1,1,0]
test = Solution()
test.sortColors(nums)  
print nums
    
