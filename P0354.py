#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:00:27 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # convert to P0300
        # dp for LIS
        dp = []
        # first sort the envelops, first by w
        # when w's are equal then sort in reversed order by h's
        # then solve the LIS by h
        # such that in this order w's are increasing
        # and smaller h is considered later to replace previous ones when w's are equal
        for h in [hh for _,hh in sorted(envelopes, key=lambda envelope: (envelope[0],-envelope[1]))]:
            # find the insertion position
            idx = bisect.bisect_left(dp, h)
            # if its the largest seem so far
            if idx == len(dp):
                # extend the list
                dp.append(h)
            # otherwise replace one element in the list
            else:
                dp[idx] = h
        # length of the list is the LIS
        return len(dp)