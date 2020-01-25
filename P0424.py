# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:36:40 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = defaultdict(int)
        l, res, mc = 0, 0, 0
        for r in xrange(len(s)):
            counts[s[r]] += 1
            mc = max(mc, counts[s[r]])
            if mc + k > res:
                res += 1
            else:
                counts[s[l]] -= 1
                l += 1                
        return res