# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:29:30 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # sort both lists from smallest to largest
        g.sort()
        s.sort() 
        # res: number of kids that can be satisfied
        # idx: index of current cookie under consideration
        # ls: number of cookies
        res, idx, ls = 0, 0, len(s)             
        # check each kid, try to find the smallest cookie that works
        for child in g:
            # in current cookie doesn't work for current kid
            # then it doesn't work for all kids after this one
            while idx < ls and child > s[idx]:
                # move on to next cookie
                idx += 1
            # if we have not passed the last cookie
            if idx < ls:
                # then current cookie is the smallest cookie that satisfy current kid
                # update count for satisfied kid
                res += 1
                # and move on to next cookie
                idx += 1
            # if we have checked the largest cookie
            else:
                # then no cookie can satisfy later kids, stop searching
                break         
        return res
            