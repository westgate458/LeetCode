# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:58:20 2020

@author: Tianqi Guo
"""

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """        
        # pigs: number of pigs needed
        # base: how many status we can generate from 1 pig, for each pig
        #       it can live until and die at each checkpoint (minutesToTest//minutesToDie checkpoints in total)
        #       or stay alive in the end (+1)
        pigs, base = 0, 1+minutesToTest//minutesToDie        
        # we place the buckets in n * n * n * ... * n dimensional array
        # for each dimension, we assign a pig to drink all buckets in the i-th row at i-th checkpoint
        # so each pig can determine the coordinate of the poison bucket in its one dimension at the end
        # for worst case scenario (we need to gaurantee to find before time is up)
        # (minutesToTest//minutesToDie+1)^pigs need to be no less than number of buckets
        # so we search for the first number that satisfies this relationship
        while (base**pigs < buckets): pigs += 1
        # number of pigs needed
        return pigs