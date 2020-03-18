# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:57:25 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """       
        # ls: the longest substring in s that ends at current character so far
        # l: length of the running substring
        # cc: previous character in p
        ls, l, cc = collections.defaultdict(int), 0, ' '       
        # check each character in p
        for c in p:                
            # if current character is an extension of the substring
            # update the length by 1             
            if ord(c) - ord(cc) in [1, -25]: l += 1                  
            # otherwise start a new substring
            else: l = 1   
            # update the max length of current character, and the previous character
            ls[c], cc = max(l, ls[c]), c            
        # mathematically, total number of substrings is the summation of all lengths
        return sum(ls.values())