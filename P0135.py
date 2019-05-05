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
        
        # current number of candies to give
        candy = 1
        # total number of candies given
        candies = 1
        
        # previous peak rating value 
        peak = 1
        # position of the previous peak
        peak_pos = 0
        
        # treat each kid
        for i in xrange(1,len(ratings)):
            # if current kid has a higher rating than previous one
            if ratings[i] > ratings[i-1]:
                # give one more candy to this kid
                candy += 1
                # update total number of candies
                candies += candy
                # update peak position
                peak_pos = i
                # update peak value
                peak = candy
            # if current kid has same rating with previous one
            elif ratings[i] == ratings[i-1]:
                # only need to give this kid 1 candy
                candy = 1
                # update total number of candies
                candies += candy
                # update peak position
                peak_pos = i
                # update peak value
                peak = candy
            # if current kid has a lower rating than previous one
            else:
                # only need to give this kid 1 candy
                candy = 1
                # calculate how far from the previous peak
                peak_dis = i - peak_pos
                # each kid between peak rating kid and current kid
                # need to be given one more candy
                # update total number of candies accordingly
                candies +=  peak_dis     
                # the peak rating kid will also need to be given one more candy
                # if it is far enough
                if peak_dis + 1 > peak:
                    # update total number of candies
                    candies += 1              
        
        # return total number of candies
        return candies
        
        
ratings = [1,3,2,2,1]
test = Solution()
print test.candy(ratings)