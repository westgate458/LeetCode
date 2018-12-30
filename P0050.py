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
        
        # in case negative power        
        if n < 0:
            # set x to its reciprocal
            x = 1/x
            # make power positive
            n = -n
            
        # set initial answer to 1
        ans = 1
        
        # convert n to binary by dividing it by 2 in each iteration
        # e.g. x^(10)_10 = x^(1010)_2 = x^(1000)_2 * x^(0010)
        # calculate x^(0000)_2, x^(0010)_2, x^(0100)_2, and x^(1000)_2 in each iteration
        # multiply answer by the power if current digit in binary expression is 1
        # stop when remaining power is 0
        while n > 0:            
            # convert n to binary expression
            # check if current digit of the binary expression is 1
            if n%2 == 1:
                # multiply answer by the power
                ans = ans * x        
                
            # half the remaining power            
            n = n / 2
            # calculate next power by setting x to its square
            x = x * x
           
        # return the answer
        return ans


x = 2.00000
n = 10

test = Solution()
print(test.myPow(x,n))