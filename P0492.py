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
        # start with the square root
        a = int(area**0.5)
        # check length a one by one, and see if it results in another integer b
        while a > 0 and area%a != 0: a -= 1
        # to keep a and b as close as possible, break the loop once integer b is found
        return([area//a,a])