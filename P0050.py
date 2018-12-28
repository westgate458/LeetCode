# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 20:55:14 2018

@author: Tianqi Guo
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        
        while n > 0:
            if n%2 == 1:
                ans = ans * x        
            n = n / 2
            x = x * x
           
        return ans


x = 2.00000
n = 10

test = Solution()
print(test.myPow(x,n))