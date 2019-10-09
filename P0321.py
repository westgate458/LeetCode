# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:27:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        def pick_k(nums, k):            
            n = len(nums)-k
            picked = []
            for num in nums:
                while picked and num > picked[-1] and n:
                    picked.pop()
                    n -= 1
                picked.append(num)
            return picked[:k]
        
        def merge(nums1, nums2):
            p1, p2, l1, l2, merged = 0, 0, len(nums1), len(nums2), []            
            while p1 < l1 and p2 < l2:
                if nums1[p1:] >= nums2[p2:]:
                    merged.append(nums1[p1])
                    p1 += 1
                else:
                    merged.append(nums2[p2])
                    p2 += 1                    
            if p1 < l1:
                merged += nums1[p1:]
            elif p2 < l2:
                merged += nums2[p2:]
            return merged
        
        l1, l2 = len(nums1), len(nums2)        
        min_from_nums1, max_from_nums1, ans = max(0, k - l2), min(l1,k), [0] * k         
         
        for k1 in range(min_from_nums1, max_from_nums1 + 1):    
            ans = max(ans, merge(pick_k(nums1, k1), pick_k(nums2, k - k1)))
        return ans
                    
                
            