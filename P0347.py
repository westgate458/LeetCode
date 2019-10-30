#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:59:24 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for num in nums: d[num] += 1
        return sorted(d, key=d.get, reverse=True)[:k]