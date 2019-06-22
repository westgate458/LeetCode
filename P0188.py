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
        # if we can do more transactions than number of days
        # it's similar to P0122. Best Time to Buy and Sell Stock II
        if k >= len(prices):
            # find pair-wise concecutive days when prices rise
            # then add the price differences up
            return sum([(b - a) for (a,b) in zip(prices[:-1],prices[1:]) if a < b])
        # if we can only do limited amount of transactions
        # it's similar to P0123. Best Time to Buy and Sell Stock III
        else:
            # money at hand if we buy i-th stock on this day            
            profit_buy = [0] + [float('-inf')] * k
            # money at hand if we sell i-th stock on this day     
            profit_sell = [0] * (k + 1)
            # check price daily
            for price in prices:  
                # try to complete the i-th transaction on this day
                for i in xrange(1,k+1):
                    
                    # money at hand if we buy the i-th stock on this day
                    # after we sell the (i-1)-th stock (on previous days)
                    profit_buy_potential = profit_sell[i-1] - price
                    # if the profit is larger than if we buy i-th stock on previous days
                    if profit_buy_potential > profit_buy[i]:
                        # update the profit
                        profit_buy[i] = profit_buy_potential  
                        
                    # money at hand if we sell the i-th stock on this day
                    # after we buy the i-th stock on previous days or on today
                    profit_sell_potential = price + profit_buy[i]  
                    # if the profit is larger than if we sell i-th stock on previous days
                    if profit_sell_potential > profit_sell[i]:
                        # update the profit
                        profit_sell[i] = profit_sell_potential
            
            # the final profit after we sell the k-th stock
            return profit_sell[-1] 

prices = [2,4,1]
k = 2

prices = [3,2,6,5,0,3]
k = 2
    
test = Solution()
print test.maxProfit(k, prices)