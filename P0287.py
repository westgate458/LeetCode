# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:04:49 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        # same algorithm as P0142 Linked List Cycle II
        # initialize two pointers: slow and fast
        p1, p2 = nums[0], nums[nums[0]]
        # stop when a loop is found
        while p1 != p2:
            # advance two pointers to the next ones
            # take the values of current nums as the new pointers
            p1, p2 = nums[p1], nums[nums[p2]]
        # restart the first pointer            
        p1 = 0
        # continue iteration until two pointers meet
        while p1 != p2:
            # advancing two pointers by 1 
            p1, p2 = nums[p1], nums[p2]
        # they met at the duplicate number
        return p1
        