# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:48:18 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Solution 1 beats 94.64%: 1-liner
        # the one that appears one more time
        # can be found by adding all orders up then finding the difference
        return chr(sum(map(ord,t))-sum(map(ord,s)))
        
        # Solution 2 beats 94.64%: string function
        for a in set(t):
            if s.count(a) < t.count(a):
                return a