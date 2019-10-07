# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:52:26 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """        
        # d: occurances of each character
        # v: if we have encountered this character before
        d, v = defaultdict(int), defaultdict(bool)
        
        # count all occurances
        for c in s:
            d[c] += 1               
        
        # result string after removal
        # initialize with '0' so we will not pop this one
        res = '0'
        # check each character
        for c in s:
            # reduce its occurance count
            d[c] -= 1
            # if we have seen this character before
            if v[c]:
                # it has already been taken care of
                continue
            # mark this one visited
            v[c] = True   
            # if previous character in answer string is larger than current one
            # and that character has more occurances after current position
            while c < res[-1] and d[res[-1]] > 0:          
                # mark it unseen
                v[res[-1]] = False
                # then we remove previous character for now, and add it back later
                res = res[:-1]
            # add current character to answer string
            res += c
        # return the string after removal
        return(res[1:])