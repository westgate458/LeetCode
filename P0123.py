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
        
        # Solution 1
        
        profit_buy_1st = float('-inf') 
        profit_sell_1st = 0
        profit_buy_2nd = float('-inf') 
        profit_sell_2nd = 0
        
        for price in prices:
                     
            # if we buy 1st stock today
            profit_buy_1st_potential = - price;
            if profit_buy_1st_potential > profit_buy_1st:
                profit_buy_1st = profit_buy_1st_potential  
                
            # if we sell 1st stock today
            profit_sell_1st_potential = price + profit_buy_1st
            if profit_sell_1st_potential > profit_sell_1st:
                profit_sell_1st = profit_sell_1st_potential      
            
            # if we buy 2nd stock today
            profit_buy_2nd_potential = profit_sell_1st - price
            if profit_buy_2nd_potential > profit_buy_2nd:
                profit_buy_2nd = profit_buy_2nd_potential
                
            # if we sell 2nd stock today
            profit_sell_2nd_potential = price + profit_buy_2nd
            if profit_sell_2nd_potential > profit_sell_2nd:
                profit_sell_2nd = profit_sell_2nd_potential
                        
        return profit_sell_2nd 
        
        
#        # Solution 2
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
