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
        # i: number of digits for current number
        # rs: total length of the sequence formed by all numbers of length i
        i, rs = 1, 9        
        # if remaining n is longer than current rs
        while n > rs:             
            # update n
            n -= rs   
            # we move on to next i
            i += 1
            # update rs as well
            rs = 9*10**(i-1)*i 
        # a few steps
        # 1) n//i: which number of length i to look at                      
        # 2) 10**(i-1) - 1 + nth: calculate this number
        # 3) n%i: which digit in this number to look at
        # 4) str(10**(i-1)-1+n//i + int(n%i>0))： convert this number to string
        # 5) finally take the digit
        return(str(10**(i-1)-1+n//i + int(n%i>0))[n%i-1])