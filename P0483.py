# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:31:21 2020

@author: Tianqi Guo
"""

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """        
        n = int(n)
        # if n is in (1111111)_b
        # then n = b^0 + b^1 + b^2 + ... + b^k = (b^(k+1)-1)/(b-1) from geometric sequence
        # largest k to try is math.log(n,2)
        # since it is the k that corresponds to base = 2
        # if base > 2, then k should be smaller
        for k in range(int(math.log(n,2)),1,-1):
            # solve for base assuming the formula holds
            b = int(n**(1./k))    
            # check if the base actually can deliver n in (1111111)_b
            # if yes just return the base, since we are looking for the smallest base
            # which corresponds to the largest k
            if ((b**(k+1))-1)/(b-1) == n: return str(b)                
        # if all k's didn't lead to reasonable base
        # n can always be represented by 1 + (n-1), which is (11)_(n-1)
        return(str(n-1))