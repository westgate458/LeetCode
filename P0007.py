# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:13:24 2018

@author: Tianqi Guo
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """       
        # store answer in y
        y = 0
        # operate digit by digit
        # continue loop if not reaching end yet
        while x != 0:
            # record previous number
            x0 = x
            # removing last digit from x
            x = int(float(x) / 10)
            # current digit is the difference
            d = x0 - x * 10    
            # add current digit to y
            y = y * 10 + d
        # check if y exceeds the range, set it to zero    
        if y < - 2**31 or y > 2**31 - 1:            
            y = 0
        
        # return result
        return(y)

x = 123
test = Solution()
print(test.reverse(x))