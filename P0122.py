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
        
        return sum([(b - a) for (a,b) in zip(prices[:-1],prices[1:]) if a < b])
        
prices = [7,1,5,3,6,4]
test = Solution()
print test.maxProfit(prices)
     
            