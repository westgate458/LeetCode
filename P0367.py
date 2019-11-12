# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:45:36 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i, j = 0, num        
        while i <= j:
            m = (i + j)//2
            m2 = m * m            
            if m2 == num:
                return True            
            elif m2 > num:                
                j = m - 1            
            else:                
                i = m + 1                
        return False
