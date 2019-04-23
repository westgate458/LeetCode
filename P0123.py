# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:51:08 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Solution 1: only one traverse
        
        # initialize tracking quantities
        # 1) money at hand if we buy 1st stock on this day
        #   start with -inf so we try buying on the first day
        profit_buy_1st = float('-inf') 
        # 2) money at hand if we sell 1st stock on this day
        #   start with 0 so we sell once current price higher than price bought
        profit_sell_1st = 0
        # 3) money at hand if we buy 2nd stock on this day
        #   start with -inf so we try buying as soon as 1st stock is sold
        profit_buy_2nd = float('-inf') 
        # 4) money at hand if we sell 2nd stock on this day
        #   start with 0 so we sell once current price higher than price bought
        profit_sell_2nd = 0
        
        # check price daily
        for price in prices:
                     
            # if we buy 1st stock today
            # price at hand would be negative current stock price
            profit_buy_1st_potential = - price;
            # update if current price lower than 
            # previous price when 1st stock was bought 
            if profit_buy_1st_potential > profit_buy_1st:
                profit_buy_1st = profit_buy_1st_potential  
                
            # if we sell 1st stock today
            # profit is the price difference
            profit_sell_1st_potential = price + profit_buy_1st
            # update if higher selling price is encountered
            if profit_sell_1st_potential > profit_sell_1st:
                profit_sell_1st = profit_sell_1st_potential      
                        
            # if we buy 2nd stock today
            # profit is money at hand after first stock is sold
            # minus current stock price
            profit_buy_2nd_potential = profit_sell_1st - price
            # update if a lower buying price for second stock is encountered
            if profit_buy_2nd_potential > profit_buy_2nd:
                profit_buy_2nd = profit_buy_2nd_potential
                        
            # if we sell 2nd stock today
            # profit is money at hand after selling 2nd stock
            profit_sell_2nd_potential = price + profit_buy_2nd
            # update final profit
            if profit_sell_2nd_potential > profit_sell_2nd:
                profit_sell_2nd = profit_sell_2nd_potential
        
        # the maximum profit after the final day
        # with two completed buy-sell transactions
        return profit_sell_2nd 
        
        
#        # Solution 2: run solution for P0121 twice
#        # once from first day, once from the last day
#        # maximum profit is the day with the highest sum of the two on that day
        
#        if not prices:
#            return 0
#        
#        l = len(prices);
#        
#        max_profit_1 = 0
#        max_profit_2 = 0
#        max_profits_1 = [0] * l
#        max_profits_2 = [0] * l       
#        min_price = float('Inf')
#        max_price = -1  
#        
#        for i in range(l):
#            
#            day_1 = i
#            day_2 = l - i - 1
#     
#            min_price = min(min_price, prices[day_1])
#            max_profit_1 = max(max_profit_1, prices[day_1] - min_price)
#            max_profits_1[day_1] = max_profit_1
#
#            max_price = max(max_price, prices[day_2])
#            max_profit_2 = max(max_profit_2, max_price - prices[day_2])
#            max_profits_2[day_2] = max_profit_2
#
#        return max([(a+b) for (a,b) in zip(max_profits_1,max_profits_2)])
        
prices = [6,1,3,2,4,7]
test = Solution()
print test.maxProfit(prices)
