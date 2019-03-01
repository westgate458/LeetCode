# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:48:37 2019

@author: Tianqi Guo
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        p = m + n - 1     
        
        while m > 0 and n > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[p] = nums2[n-1]
                n = n - 1
                p = p - 1                
            else:
                nums1[p] = nums1[m-1]
                m = m - 1
                p = p - 1       
                
        if m == 0:
            nums1[:n] = nums2[:n]       
            
        return  

nums1 = [0]
m = 0
nums2 = [1]
n = 1

test = Solution()
test.merge(nums1, m, nums2, n)
print(nums1)