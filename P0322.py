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
        # check a trivial case: amount can be formed by max coin value only
        coin_max = max(coins)
        if amount % coin_max == 0:
            return amount//coin_max
        
        # dictionary[amount]: minimum number of coins
        d = {0:0}
        
        # check all amounts below target
        for n in xrange(amount+1):
            # if current amount can be achieved
            if n in d:                
                # update all amount that can be achieved from current amount
                for coin in coins:                
                    # next amount formed by adding one new coin
                    next_amount = n + coin
                    # check if the new amount is formed by fewer number of coins
                    if (next_amount not in d) or (d[next_amount] > d[n] + 1):
                        # update the dictionary entry
                        d[next_amount] = d[n] + 1    
        # if target amount can be achieved
        if amount in d:
            # return the minimum number of coins
            return d[amount]
        else:        
            return -1