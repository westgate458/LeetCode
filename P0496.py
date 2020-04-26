# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:13:59 2020

@author: Tianqi Guo
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d, s = {}, [float('inf')]        
        for n in nums2:
            while s[-1] < n: d[s.pop()] = n
            s.append(n)              
        return [d.get(n, -1) for n in nums1]