# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:48:00 2019

@author: Tianqi Guo
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Solution 1 beats 61.44%: bit operation
        # deal with trivial case
        if n <= 0:
            return False        
        # continue bit-shift right until last digit
        while n > 1:
            # if current n cant be divided by 2
            if n%2 != 0:
                # it is not a power of two
                return False
            # shift right
            n = n >> 1   
        # if all intermediate n's are power of 2
        # original n is power of 2
        return True        
        
        # Solution 2 beats 84.81%: cheat by built-in functions                
        return len(bin(n).rstrip('0'))==3

n = 16        
test = Solution()
print(test.isPowerOfTwo(n))

