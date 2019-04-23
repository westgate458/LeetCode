# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:27:59 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # 1) accumulate profit if price continues to rise
        #   if prices are [1, 2, 3], 
        #   buy at 1 then sell at 2, buy at 2 then sell at 3
        #   is equal to buy at 1 then sell at 3
        # 2) do not sell or buy if price drops
        #   if prices are [3, 2, 1], no profit can be made
        # so we only need to find pair-wise concecutive days when prices rise
        # then add the price differences up
        
        return sum([(b - a) for (a,b) in zip(prices[:-1],prices[1:]) if a < b])
        
prices = [7,1,5,3,6,4]
test = Solution()
print test.maxProfit(prices)
     
            