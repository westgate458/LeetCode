# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:13:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        h, t = 0, len(nums) - 1        
        while h <= t:
            if nums[h] <= nums[t]:
                return nums[h]            
            m = (h + t)//2            
            if nums[h] > nums[m]:
                t = m
            else:          
                h = m + 1

nums = [3,4,5,1,2]  
nums = [4,5,6,7,0,1,2]       
nums = [2, 1]
nums = [3, 1, 2]
test = Solution()
print test.findMin(nums)
                
                
                
            