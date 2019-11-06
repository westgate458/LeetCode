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
        dp = []
        for h in [hh for _,hh in sorted(envelopes, key=lambda envelope: (envelope[0],-envelope[1]))]:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)