# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:06:48 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # sum of all number and length of array
        s, l = sum(A), len(A)             
        # calculate f(0)
        ss = ans = sum([A[i]*i for i in range(l)])       
        # get f(k) from f(k-1)
        for i in range(l-1,-1,-1):        
            # the formula
            ss = s + ss - l * A[i] 
            # update the max
            if ss > ans: ans = ss                        
        # return the max
        return ans