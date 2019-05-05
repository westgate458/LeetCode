# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:27:03 2019

@author: Tianqi Guo
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        # Solution 1        
        # no soluition if total cost is larger than total gas available
        if sum(gas) < sum(cost):
            return -1
        
        # residual gas in tank, and starting point
        res, start = 0, 0        
        
        # check each station
        for i in range(len(gas)):
            # update residual gas in tank
            res += gas[i] - cost[i]
            # if residual is negative
            # we can not get to next station
            # and all previous stations can not be the starting point
            # since for each previous station we needed non-negative residual gas from earlier stations
            # to get to current position
            if res < 0:
                # start from next station with 0 residual gas in tank
                res = 0
                start = i + 1
        
        # for the 2nd segment (from start position till end) we have sum(gas)_1 - delta_1 = sum(cost)_1
        # and for the other half (1st segment) we have sum(gas)_2 + delta_2 = sum(cost)_2
        # so sum(gas)_1 + sum(gas)_2 + delta_2 - delta_1 = sum(cost)_1 + sum(cost)_2
        # i.e. sum(gas) - sum(cost) = delta_1 - delta_2 >= 0
        # we have delta_1 >= delta_2
        # so the residual gas after the 2nd segment is sufficient to cover 
        # the deficiency in the 1st segment to make the round trip

        # return the starting point                
        return start
            
        
        
#        # Solution 2
#        res = 0
#        start = 0    
#        l = len(gas)
#        c = 0
#        p = 0
#        
#        while start < l:      
#                        
#            res = res + gas[p] - cost[p]       
#            
#            if res >= 0:
#                p += 1
#                c += 1
#                if p == l:
#                    p = 0
#                if c == l:
#                    return start
#            else:
#                if start > p:
#                    break
#                start = p + 1
#                p = start
#                res = 0
#                c = 0             
#            
#        return -1
     
        

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

#gas  = [1,2,3,4,3,2,4,1,5,3,2,4]
#cost = [1,1,1,3,2,4,3,6,7,4,3,1]
        
test = Solution()
print test.canCompleteCircuit(gas, cost)