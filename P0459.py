# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:47:41 2020

@author: Tianqi Guo
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Solution 1 beats 89.94%: interesting observation
        # somehow, this holds
        return s in (s+s)[1:-1]
    
        # Solution 2 beats 69.55%: check all possible substrings
        p, l = 1, len(s)
        while p <= l:
            while l%p != 0: p += 1
            if p == l: return False                      
            pp = p          
            while pp < l and s[pp:pp+p] == s[:p]: pp += p                
            if pp == l: return True
            p += 1
        return False
        