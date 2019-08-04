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
        if n <= 0:
            return False        
        while n > 1:
            if n%2 != 0:
                return False
            n = n >> 1            
        return True        
        
        # Solution 2 beats 84.81%: cheat by built-in functions                
        return len(bin(n).rstrip('0'))==3

n = 16        
test = Solution()
print(test.isPowerOfTwo(n))

