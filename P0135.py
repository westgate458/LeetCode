# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:53:31 2019

@author: Tianqi Guo
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        candy = 1
        candies = 1
        
        peak = 1
        peak_pos = 0
        
        for i in xrange(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy += 1
                candies += candy
                peak_pos = i
                peak = candy
            elif ratings[i] == ratings[i-1]:
                candy = 1
                candies += candy
                peak_pos = i
                peak = candy
            else:
                candy = 1
                peak_dis = i - peak_pos
                candies +=  peak_dis                
                if peak_dis + 1 > peak:
                    candies += 1              

        return candies
        
        
ratings = [1,3,2,2,1]
test = Solution()
print test.candy(ratings)