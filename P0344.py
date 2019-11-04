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
        # the pointers at both ends
        i, j = 0, len(s)-1
        # stop swapping until two pointers meet
        while (i < j):
            # swap two elements
            s[i], s[j] = s[j], s[i]
            # update pointers
            i += 1
            j -= 1