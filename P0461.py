# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:41:30 2020

@author: Tianqi Guo
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # c: compare each bit by xor
        # res: number of different 
        c, res = x^y, 0        
        # count how many bits of c is 1
        while c: res, c = res+(c&1), c>>1
        return res