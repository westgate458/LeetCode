# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:32:52 2019

@author: Tianqi Guo
"""

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # convertnums into strings then sort them
        return(sorted(map(str,range(1,n+1))))