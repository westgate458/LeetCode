# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:51:58 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1        
        k -= 1
        while k > 0:
            left, right, step = cur, cur + 1, 0            
            while left <= n:
                step += min(right, n+1) - left 
                left, right = 10*left, 10*right                
            if step <= k:
                k -= step
                cur += 1
            else:
                k -= 1
                cur *= 10
        return(cur)