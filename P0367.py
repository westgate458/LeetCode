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
        # binary search for the root
        i, j = 0, num        
        # continue search until ends meet
        while i <= j:
            # take the mid
            m = (i + j)//2
            # try the square
            m2 = m * m    
            # check if root is found
            if m2 == num:
                return True            
            # adjust ends accordingly
            elif m2 > num:                
                j = m - 1            
            else:                
                i = m + 1            
        # if no root is found then it is not a perfect square
        return False
