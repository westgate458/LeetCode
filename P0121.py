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
        
        max_profit = 0
        min_price = float('Inf')
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
                
        return max_profit
    
prices = [7,1,5,3,6,4]    
test = Solution()
print test.maxProfit(prices)

                
        

