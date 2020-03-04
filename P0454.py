# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:30:24 2020

@author: Tianqi Guo
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """        
        # res: count of combinations
        # s: all possible sums of number pairs from (A,B)
        res, s = 0, collections.defaultdict(int)        
        # for all number pairs from (A,B)   
        for a in A:
            for b in B:
                # update the occurance count for its sum     
                s[a+b] += 1
        # for all number pairs from (C,D)
        for c in C:
            for d in D:
                # check if its counter part exists in s
                if -(c+d) in s:
                    # if yes, update the counts for the 0-sum combination
                    res += s[-c-d]
        return res