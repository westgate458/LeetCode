# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:43:51 2019

@author: Tianqi Guo
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # rootfinding of f(a) = a^2 - x = 0
        # by Newton's method
        
        # deal with trivial case
        if x == 0:
            return 0
        
        # take x as float
        x = float(x)
        # start iteration with a = x
        a = x
        # flag if this iteration has the same integer value of a
        # as the previous iteration
        flag = True
        # continue iteration while a still changing
        while flag:
            # new a as b from Newton's method
            b = (a + x/a)/2 
            # compare the integer parts
            flag = (int(a) != int(b))  
            # update value of a
            a = b   
            
        # return the integer part of a
        return int(a)
    
    

x = 8
test = Solution()
print test.mySqrt(x)