# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:02:23 2018

@author: Tianqi Guo
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # length of list and deal with trivial case
        l = len(nums)
        if l <= 1:
            return None
        
        # start from the end of the list
        # find the first number num[p] that is smaller than its right neighbor
        p = l - 2
        while (p >=0) and (nums[p]>= nums[p+1]):            
            p = p - 1
        
        # if already the last permutation
        # i.e. nums already sorted in descending order
        if p == -1:            
            # return the first permutation
            # i.e. sort nums in ascending order
            nums.sort()            
            return None            
        else:
            # start from the end of the list
            # find the first element that is larger than num[p]
            q = l - 1
            while nums[p] >= nums[q]:
                q = q - 1
            
            # swap the two nums            
            nums[p], nums[q] = nums[q], nums[p]
            # reverse nums in between            
            ll = (l - 1 - p)/2
            for q in range(0,ll):
                nums[p+1+q], nums[l-1-q] = nums[l-1-q], nums[p+1+q]
                
        return None
                
nums = [1,2,4,3]        
test = Solution()
test.nextPermutation(nums)
print(nums)
        