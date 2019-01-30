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
        if x == 0:
            return 0
        
        x = float(x)
        a = x
        flag = True
        while flag:
            b = (a + x/a)/2 
            flag = (int(a) != int(b))    
            a = b   

        return int(a)
    
    

x = 8
test = Solution()
print test.mySqrt(x)