# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:20:29 2019

@author: Tianqi Guo
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """              
        # deal with trivial case:
        # if current length is shorter than k
        # then the length of the longest substring is 0
        if len(s) < k:
            return 0         
        # check each character in s
        for c in set(s):
            # if current character appears less than k times            
            if s.count(c) < k:  
                # this character cant be part of the substring
                # split s at all positions of this character
                # then pick the longest substring from the split ones that satisfy the requirement
                # divide by character into subproblems and conquer
                return(max([self.longestSubstring(ss, k) for ss in s.split(c)]))
        # if all characters in s appear no less than k times            
        # no need to split, current string is what we look for
        return len(s)