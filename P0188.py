# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:29:44 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """        
        if k >= len(prices):
            ans = 0
            for i in xrange(1,len(prices)):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
        else:
            profit_buy = [0] + [float('-inf')] * k
            profit_sell = [0] * (k + 1)
            for price in prices:  
                for i in xrange(1,k+1):
                    profit_buy_potential = profit_sell[i-1] - price;
                    if profit_buy_potential > profit_buy[i]:
                        profit_buy[i] = profit_buy_potential  
                    profit_sell_potential = price + profit_buy[i]  
                    if profit_sell_potential > profit_sell[i]:
                        profit_sell[i] = profit_sell_potential
            return profit_sell[-1] 

prices = [2,4,1]
k = 2

prices = [3,2,6,5,0,3]
k = 2
    
test = Solution()
print test.maxProfit(k, prices)