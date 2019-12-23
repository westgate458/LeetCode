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
        if len(s) < k:
            return 0         
        for c in set(s):
            if s.count(c) < k:  
                return(max([self.longestSubstring(ss, k) for ss in s.split(c)]))
        return len(s)