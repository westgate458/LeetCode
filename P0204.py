# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 19:41:14 2019

@author: Tianqi Guo
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """        
        isPrime = [False, False] + [True] * (n - 2)                
        for num in xrange(2,int(n**0.5)+1):            
            if isPrime[num]:     
                isPrime[num**2:n:num] = [False] * len(xrange(num**2,n,num)) 
        return sum(isPrime)

