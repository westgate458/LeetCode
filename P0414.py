# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:58:40 2020

@author: Tianqi Guo
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1 beats 95.85%: cheat by sorting
        nums = set(nums)
        if len(nums) >= 3:
            return(sorted(nums)[-3])
        else:
            return(max(nums))
        
        # Solution 2 beats 95.85%: simple O(n)
        n1 = n2 = n3 = float('-inf')
        for num in set(nums):
            if num > n1:
                n3, n2, n1 = n2, n1, num  
            elif num > n2:
                n3, n2 = n2, num
            elif num > n3:
                n3 = num
        if n3 > float('-inf'):
            return n3
        else:
            return n1