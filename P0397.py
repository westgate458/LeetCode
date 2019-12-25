# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:46:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = {1:0}        
        def replace(n):            
            if n not in self.d:
                if n%2 == 0:
                    self.d[n] = replace(n/2) + 1
                else:
                    self.d[n] = min(replace(n+1), replace(n-1)) + 1
            return self.d[n]        
        return replace(n)