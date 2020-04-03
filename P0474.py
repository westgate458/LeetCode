# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:21:29 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Solution 1 beats 90.53%: bottom-up dp
        # dp[(x,y)]:z with x zeros and y ones, z is the max number of strings that we can form
        # res: max number of strings that we can form in the end
        dp, res = {(0,0):0},0  
        # first, for each string in strs, we count its 0 and 1 -> 2d costs
        # then we build dp by taking one more string into consideration each time
        for c0, c1 in map(lambda s:(s.count('0'), s.count('1')),strs):   
            # we look back into strings already accounted for
            # if we want to add current string into previous solution
            # then previous cost of 0 must be in the range (0, m-c0)
            # and  previous cost of 1 must be in the range (0, n-c1)
            # such that after we add current string, total costs wont exceed [m, n]
            # we build it backwards, so current string wont be used twice in any solution
            # since each time dp[(i,j)] will be from previous loop unchanged
            for i in xrange(m-c0,-1,-1):                          
                for j in xrange(n-c1,-1,-1):
                    # if previous solution exists (base case (0,0) will always exist)
                    if (i,j) in dp:
                        # then we have a new potential solution with costs (i+c0,j+c1)
                        # if solution for (i+c0,j+c1) already exists, we update it if with current string added, 
                        # [number of strings from (i,j)] + 1 is more than previous solution for (i+c0,j+c1)
                        dp[(i+c0,j+c1)] = max(dp.get((i+c0,j+c1),0),dp[(i,j)]+1)
                        # also update res since max number of string may not be solution for [m,n] in the end
                        res = max(res, dp[(i+c0,j+c1)])
        # the max number of strings found
        return res
    
        # Solution 2 beats 87.57%: top-bottom dp
        costs = [(s.count('0'), s.count('1')) for s in strs]       
        self.dp = {(0,0):(0,0)}
        def DFS(m, n):            
            if (m, n) not in self.dp:  
                c, t = 0, 0            
                for i, cost in enumerate(costs):   
                    code = 1 << i
                    if (cost[0] <= m) and (cost[1] <= n):                     
                        tt, cc = DFS(m-cost[0], n-cost[1]) 
                        cc += not(tt&code)
                        if cc > c:
                            c, t = cc, tt|code                            
                self.dp[(m,n)] = (t,c)            
            return self.dp[(m,n)]  
        return DFS(m, n)[1]