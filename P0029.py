# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:13:24 2018

@author: Tianqi Guo
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # take absolute value, deal with sign in the end
        N = abs(dividend)
        n = abs(divisor)
        sign = ((dividend >= 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0))
        
        # pre-processing: calculate all values of n*2^c
        # start with n*2^0 as first element
        sums = [n] 
        # times of double, i.e. exponent of 2
        c = 0
        # double sum until it is larger than dividend
        while sums[c] + sums[c] <= N + N:                          
            # double the divisor, i.e. multiple by 2
            sums.append(sums[c] + sums[c])
            # increase exponent of 2 by 1
            c = c + 1        

        # calculate quotient
        # remaining of dividend                
        remaining = N
        # the quotient
        q = 0
        # taking n*2^c away from remaining
        # until remaining is smaller than divisor
        while remaining >= n: 
            # look for largest n*2^c 
            # that is smaller than remaining
            c = 0
            while sums[c+1] < remaining:
                c = c + 1
            # add 2^c to the quotient
            q = q + 2**c
            # take n*2^c away from remaining
            remaining = remaining - sums[c]        
        
        # deal with sign
        if not sign:
            q = - q
            
        # deal with overflow
        if (q < -2**31) or (q > 2**31 - 1):
            return 2**31 - 1
        else:
            return q
    

dividend = 10
divisor = 3
test = Solution()
print(test.divide(dividend, divisor))