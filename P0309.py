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
        # at each time step, we have three options
        # for each option we have a state function
        # hold is initialized as -inf so we will always buy on the first day
        hold, sold, cold = float('-inf'), 0, 0 
        # for each day we update the states as follows
        for i in xrange(len(prices)):            
            # hold:
            # two scenarios where we hold stock on this day:
            # 1) we continue holding the same stock from yesterday
            # 2) yesterday was on colddown (or on rest), and we buy stock today
            # sold:
            # one scenario where we sell stock on this day:
            # 1) we held stock yesterday and sell it today
            # cold:
            # two scenarios where we are on colddown or on rest on this day:
            # 1) we just sold stock yesterday so we can do nothing today
            # 2) we decide to wait one more day (on rest)
            hold, sold, cold = max(hold, cold - prices[i]), hold + prices[i], max(cold, sold) 
        # after the final day, the max profit is from the two states:
        # we just sold the last stock, or we were on colddown
        return max(sold, cold)