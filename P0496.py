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
        # d: next greater element for each number in nums2
        # s: monotonically decreasing stack
        d, s = {}, [float('inf')]    
        # for each number in nums2, find all numbers before it that is smaller
        for n in nums2:
            # keep popping the stack, until the last element is not smaller than current number
            # for each popped number, current number is the next greater element for it
            while s[-1] < n: d[s.pop()] = n
            # push current number into stack
            s.append(n)              
        # for each number in nums1, now retreive its next greater element from d
        return [d.get(n, -1) for n in nums1]