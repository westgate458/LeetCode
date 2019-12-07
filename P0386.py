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
        return(sorted(map(str,range(1,n+1))))