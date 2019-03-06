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
        
        # length of the merged list
        # p, m, n serve as pointers starting from the tail of each list
        p = m + n - 1     
        
        # continue merging until one of the lists is empty
        while m > 0 and n > 0:
            
            # if current number in 2nd list is larger
            if nums2[n-1] >= nums1[m-1]:
                # place it in the merged list
                nums1[p] = nums2[n-1]
                # updatge the pointers
                n = n - 1
                p = p - 1   
            # if current number in 1st list is larger
            else:
                # place it in the merged list
                nums1[p] = nums1[m-1]
                # updatge the pointers
                m = m - 1
                p = p - 1       
        
        # if the 1st list has no remaining numbers
        if m == 0:
            # place the remaining numbers from 2nd list into the merged list
            nums1[:n] = nums2[:n]       
        
        # return nothing since numbers are merged in-place
        return  

nums1 = [0]
m = 0
nums2 = [1]
n = 1

test = Solution()
test.merge(nums1, m, nums2, n)
print(nums1)