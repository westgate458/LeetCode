# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:23:31 2020

@author: Tianqi Guo
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = max(len(num1),len(num2))
        num1, num2, carry, res = num1.zfill(l), num2.zfill(l), 0, ''
        for i in xrange(l-1,-1,-1):      
            carry, digit = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
            res += str(digit)
        if carry:
            res += str(carry)
        return res[::-1]
            