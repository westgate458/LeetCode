# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:05:47 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        hold, sold, cold = float('-inf'), 0, 0 
        for i in xrange(len(prices)):            
            hold, sold, cold = max(hold, cold - prices[i]), hold + prices[i], max(cold, sold) 
        return max(sold, cold)