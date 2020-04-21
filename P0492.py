# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:29:51 2020

@author: Tianqi Guo
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        a = int(area**0.5)
        while a > 0 and area%a != 0: a -= 1
        return([area//a,a])