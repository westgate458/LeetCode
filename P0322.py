# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:55:08 2019

@author: Tianqi Guo
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """        
        coin_max = max(coins)
        if amount % coin_max == 0:
            return amount//coin_max
        
        d = {0:0}
        
        for n in xrange(amount+1):
            if n in d:                
                for coin in coins:                
                    next_amount = n + coin
                    if (next_amount not in d) or (d[next_amount] > d[n] + 1):
                        d[next_amount] = d[n] + 1                
        if amount in d:
            return d[amount]
        else:        
            return -1