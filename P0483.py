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
        for k in range(int(math.log(n,2)),1,-1):
            b = int(n**(1./k))    
            if ((b**(k+1))-1)/(b-1) == n: return str(b)                
        return(str(n-1))