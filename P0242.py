# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:11:34 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # two strings are anagrams if and only if 
        # after the characters are sorted, two strings are identical
        return sorted(s) == sorted(t)