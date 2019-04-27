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
        if sum(gas) < sum(cost):
            return -1
        
        res, start = 0, 0        
        
        for i in range(len(gas)):
            res += gas[i] - cost[i]
            if res < 0:
                res = 0
                start = i + 1
                
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