# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 20:44:18 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """        
        i, rs = 1, 9        
        while n > rs:             
            n -= rs             
            i += 1
            rs = 9*10**(i-1)*i                       
        return(str(10**(i-1)-1+n//i + int(n%i>0))[n%i-1])