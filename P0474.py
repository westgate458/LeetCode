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
        dp, res = {(0,0):0},0        
        for c0, c1 in map(lambda s:(s.count('0'), s.count('1')),strs):   
            for i in xrange(m-c0,-1,-1):                          
                for j in xrange(n-c1,-1,-1):
                    if (i,j) in dp:
                        dp[(i+c0,j+c1)] = max(dp.get((i+c0,j+c1),0),dp[(i,j)]+1)
                        res = max(res, dp[(i+c0,j+c1)])
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