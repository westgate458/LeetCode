# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:41:05 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # max profit so far
        max_profit = 0
        # minimum price encountered so far
        min_price = float('Inf')
        
        # check price daily
        for price in prices:
            # update the min price so far
            min_price = min(min_price, price)
            # update max profit if selling the stock today
            max_profit = max(max_profit, price - min_price)
        
        # return max profit in the end
        return max_profit
    
prices = [7,1,5,3,6,4]    
test = Solution()
print test.maxProfit(prices)

                
        

