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
        
        N = abs(dividend)
        n = abs(divisor)
        sign = ((dividend >= 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0))
        
        sums = [n] 
        c = 0
        while sums[c] + sums[c] <= N + N:                          
            sums.append(sums[c] + sums[c])
            c = c + 1        
                
        remaining = N
        q = 0
        while remaining >= n: 
            c = 0
            while sums[c+1] < remaining:
                c = c + 1
            q = q + 2**c
            remaining = remaining - sums[c]        
        
        if not sign:
            q = - q
            
        if (q < -2**31) or (q > 2**31 - 1):
            return 2**31 - 1
        else:
            return q
    

dividend = 10
divisor = 3
test = Solution()
print(test.divide(dividend, divisor))