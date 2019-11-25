# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:26:25 2019

@author: Tianqi Guo
"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """    
        # answer and current state
        ans, f = 1, a % 1337
        # start from the lowest digit
        for n in b[::-1]:
            # from current state, using formula to get next state
            ans, f = (((f ** n) % 1337) * ans) % 1337, (f ** 10) % 1337
        # return final answer
        return ans