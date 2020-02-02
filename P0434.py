# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:19:23 2020

@author: Tianqi Guo
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return(sum([a != ' ' and b == ' ' for a, b in zip(s,s[1:]+' ')]))