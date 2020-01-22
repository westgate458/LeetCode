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
        # length of the longer one
        l = max(len(num1),len(num2))
        # first pad the shorter one to have the same length
        # then initialize the answer string and the carry
        num1, num2, carry, res = num1.zfill(l), num2.zfill(l), 0, ''
        # add digits from the least significants
        for i in xrange(l-1,-1,-1):      
            # update result for current digit and the carry
            carry, digit = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
            # update answer string
            res += str(digit)
        # deal with the remaining carry
        if carry:
            res += str(carry)
        # result string in reversed order so the least significant digit is on the right
        return res[::-1]
            