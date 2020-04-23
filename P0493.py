# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:45:47 2020

@author: Tianqi Guo
"""

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        def merge(nums):            
            l = len(nums)
            if l == 1:
                return nums
            else:
                left, right = merge(nums[:l//2]), merge(nums[l//2:])
                l1, l2 = l//2, l - l//2                
                i = j = 0
                while i < l1 and j<l2:
                    while i < l1 and left[i] <= right[j]*2: i += 1
                    self.res += l1 - i
                    j += 1                   
                return sorted(left+right)
        if not nums:
            return 0
        else:
            self.res = 0
            merge(nums)        
            return self.res