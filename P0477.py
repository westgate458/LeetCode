# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:43:09 2020

@author: Tianqi Guo
"""

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        # Solution 1 beats 96.45%: one-liner        
        return(sum([b.count('0')*b.count('1') for b in zip(*map('{:032b}'.format, nums))]))
        
        # Solution 2 beats 54.61%: same approach, different implementation
        ones = collections.defaultdict(int)        
        for num in nums:
            p = 0
            while num:
                ones[p] += num&1
                num >>= 1
                p += 1                    
        res = 0
        l_nums = len(nums)
        for one in ones.values():
            res += one * (l_nums-one)
        return res