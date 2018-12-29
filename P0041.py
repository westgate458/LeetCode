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
        
        # remove all negative and zero elements first
        # use sign to mark appearance of elements afterwards
        p = 0
        while p <= len(nums) - 1:
            if nums[p] <= 0:
                nums.pop(p)
            else:
                p = p + 1
        
        # numebr of remaining positives        
        l = len(nums)
        # examine each element
        for i in range(l):
            # take the abs value of the current number            
            num_abs = abs(nums[i])
            # if the abs value is smaller than the number of elements
            # meaning it should appear
            if  (num_abs <= l) and (nums[num_abs - 1] > 0):
                # mark the element x as 'appeared'
                # by changing the sign of the x-th element to negative
                nums[num_abs - 1] = - nums[num_abs - 1]        
                
        # look for the first element with a positive sign in xth position 
        # meaning number x is missing        
        for i in range(l):
            if nums[i] > 0:
                return i + 1   
            
        # if all elements (1st to l-th) are negative
        # meaning numbers from 1 to l all exist
        # then first missing number is l + 1
        return l + 1

nums = [1,2,4]  
test = Solution()
print(test.firstMissingPositive(nums)) 