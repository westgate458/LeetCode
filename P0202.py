# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:42:13 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """        
        d = {}
        while n not in d:
            if n == 1:
                return True
            d[n] = True
            m = 0
            while (n):
                m += (n%10) ** 2
                n /= 10            
            n = m
        return False



n = 99      
n = 19  
test = Solution()
print test.isHappy(n)