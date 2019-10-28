#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:33:15 2019

@author: Tianqi Guo
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while (i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1