# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:23:39 2018

@author: Tianqi Guo
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        p = 0
        while p <= len(nums) - 1:
            if nums[p] <= 0:
                nums.pop(p)
            else:
                p = p + 1
                
        l = len(nums)
        for i in range(l):
            num_abs = abs(nums[i])
            if  (num_abs <= l) and (nums[num_abs - 1] > 0):
                nums[num_abs - 1] = - nums[num_abs - 1]        
                
        
        for num in nums:
            if num > 0:
                return i+1     
       
        return l + 1

nums = [1,1]  
test = Solution()
print(test.firstMissingPositive(nums)) 