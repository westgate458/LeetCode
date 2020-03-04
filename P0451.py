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
        # the count of occurances for each character
        d = defaultdict(int)
        # count each character
        for c in s: d[c] += 1
        # steps:
        # 1) form tuples (occurance, character)
        # 2) sort all tuples based on occurances from high to low
        # 3) construct strings by occurance*character
        # 4) join all strings to form the result
        return(''.join([j*i for i, j in sorted(zip(d.values(), d.keys()),reverse=True)]))