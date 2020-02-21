# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:06:53 2020

@author: westg
"""

from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = defaultdict(int)
        for c in s: d[c] += 1
        return(''.join([j*i for i, j in sorted(zip(d.values(), d.keys()),reverse=True)]))