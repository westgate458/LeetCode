# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:19:49 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = [0]*len(nums)
        res = []
        for num in nums:
            if visited[num-1]:
                res.append(num)
            else:
                visited[num-1] = 1
        return res