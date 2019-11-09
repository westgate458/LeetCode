# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:54:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """                
        # deal with trivial case
        if not n : return 1
        # all numbers of lengths longer than 10 cant have unique digits
        if n > 10: n = 10                
        # f[n]: number with unique digits of length (n+1)
        f = [10] + [9] * (n-1)        
        # calculate for each length
        for i in xrange(1, n):     
            # from permutation, each digit can be chosen from 10, 9, 8, ..., 1 numbers
            # but the leading digit can't be 0
            c = 10 - i
            # calculate the permutaion
            while c < 10:
                f[i] *= c
                c += 1
        # summation is the total 
        return sum(f)