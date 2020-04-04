# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:43:26 2020

@author: Tianqi Guo
"""

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, s = 0, [1]        
        while len(s) < n:            
            s += [s[-1]] * (s[i]-1)                     
            s += [s[-1]^3] 
            i += 1       
        return(s[:n].count(1))