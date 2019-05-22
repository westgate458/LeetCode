# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:48:37 2019

@author: Tianqi Guo
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        h, t = 0, len(nums) - 1
        while h < t:
            m = (h + t)//2 
            if nums[t] > nums[m]:
                t = m
            elif nums[t] < nums[m]:  
                h = m + 1
            else:
                t -= 1
        return nums[h] 

        
                
nums = [3,4,5,1,2]  
nums = [4,5,6,7,0,1,2]       
nums = [2, 1]
nums = [3, 1, 2]
nums = [2,2,2,0,1]
nums = [3,1,3]
nums = [1,2,3]


nums = [2,2,2,0,1]
nums = [1,1,3,1]
nums = [1]

test = Solution()
print test.findMin(nums)