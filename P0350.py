# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:29:24 2019

@author: Tianqi Guo
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # Solution 1 beats 93.84%: using dictionary
        from collections import defaultdict
        d, ans = defaultdict(int), []        
        for num in nums1:
            d[num] += 1
        for num in nums2:
            if d.get(num, 0) > 0:
                ans.append(num)
                d[num] -= 1
        return ans
        
#        # Solution 2 beats 80.45%: sort arrays first
#        i, j, l1, l2, ans = 0, 0, len(nums1), len(nums2), []       
#        nums1.sort()
#        nums2.sort()
#        
#        while i < l1 and j < l2:
#        
#            if nums1[i] < nums2[j]:
#                i += 1
#
#            elif nums1[i] > nums2[j]:
#                j += 1
#
#            else:
#                ans.append(nums1[i])
#                i, j = i + 1, j + 1                
#        
#        return ans