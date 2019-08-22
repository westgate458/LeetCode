# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:50:27 2019

@author: Tianqi Guo
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return num - (num - 1)//9 * 9