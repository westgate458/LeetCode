class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m, res = float('inf'), 0        
        for price in prices:
            if price - m > res: res = price - m          
            if price < m: m = price           
        return res