# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:49:10 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """             
        # solution 1 beats 99.69%: try-except
        # last position of found matching
        last = -1
        # check each character in s
        for c in s:
            # try to locate this character in t
            try:
                # look for its location starting from last matched point
                last = t.index(c, last+1)
            # if not found, then s is not a subsequence of t
            except:
                return False
        # since all characters from s exist in t following the same order
        # s is a subsequence of t
        return True
        
        # solution 2 beats 72.07%: naive search
        s_s = set(s)
        t = [c for c in t if c in s_s]
        ps, pt, ls, lt = 0, 0, len(s), len(t)        
        while ps < ls and pt < lt:
            if s[ps] == t[pt]: ps += 1
            pt += 1        
        return ps == ls
            
            