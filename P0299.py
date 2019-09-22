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
        # number of bulls and cows
        A, B = 0, 0        
        # number of each characters occurring in two strings
        seen_s, seen_g = defaultdict(int), defaultdict(int) 
        # compare each character
        for i, j in zip(secret, guess):
            # if two characters are the same
            if i == j:
                # number of rights +1
                A += 1
            # if two characters are different
            else:
                # update the number of occurances
                seen_s[i] += 1
                seen_g[j] += 1
        # check all characters that have occured
        for key in set(seen_s).intersection(set(seen_g)):
            # for each character, number of wrong placements are then
            # updated by the min of occurances in two strings
            B += min(seen_s[key],seen_g[key])
        # return the answer in required format
        return str(A)+'A'+str(B)+'B'