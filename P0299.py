# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:17:37 2019

@author: westg
"""

from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0        
        seen_s, seen_g = defaultdict(int), defaultdict(int)        
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                seen_s[i] += 1
                seen_g[j] += 1
        for key in set(seen_s).intersection(set(seen_g)):
            B += min(seen_s[key],seen_g[key])
        return str(A)+'A'+str(B)+'B'