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
        s, l = sum(A), len(A)             
        ss = ans = sum([A[i]*i for i in range(l)])       
        for i in range(l-1,-1,-1):        
            ss = s + ss - l * A[i] 
            if ss > ans: ans = ss                        
        return ans