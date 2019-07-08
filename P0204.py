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
        # whether each number is a prime number
        isPrime = [False, False] + [True] * (n - 2)                
        # for each prime number under sqrt(n)
        for num in xrange(2,int(n**0.5)+1):            
            # if current number is a prime number
            if isPrime[num]:     
                # cross off its multiples from num^2 till end
                isPrime[num**2:n:num] = [False] * len(xrange(num**2,n,num)) 
        # sum of list is the number of prime numbers
        return sum(isPrime)

