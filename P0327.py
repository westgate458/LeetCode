# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:06:04 2019

@author: Tianqi Guo
"""

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
                    
        def merge(i, j):            
            if i >= j:
                return 0            
            m = (i + j)//2            
            ans = merge(i, m) + merge(m+1, j)            
            k1 = k2 = m + 1
            for sum_i in sums[i:m+1]:             
                while k1 <= j and sums[k1] - sum_i < lower:                    
                    k1 += 1                
                while k2 <= j and sums[k2] - sum_i <= upper:                                
                    k2 += 1             
                ans += k2 - k1 
            sums[i:j+1] = sorted(sums[i:j+1])
            return ans
        
        l = len(nums)
        sums = [0] * (l+1)        
        for i in xrange(1,l+1):
            sums[i] = sums[i-1] + nums[i-1]   
        return merge(0, l)
                    
                    