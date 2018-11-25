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
        l = len(nums)
        if l <= 1:
            return None
        
        p = l - 2
        while (p >=0) and (nums[p]>= nums[p+1]):
            p = p - 1
        
        if p == -1:
            
            nums.sort()
            
            return None
            
        else:
            q = l - 1
            while nums[p] >= nums[q]:
                    q = q - 1
           
            if p != q:
                nums[p], nums[q] = nums[q], nums[p]
                ll = (l - 1 - p)/2
                for q in range(0,ll):
                    nums[p+1+q], nums[l-1-q] = nums[l-1-q], nums[p+1+q]
       
        return None
                
nums = [1,1]        
test = Solution()
test.nextPermutation(nums)
print(nums)
        