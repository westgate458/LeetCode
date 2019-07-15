# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:20:55 2019

@author: Tianqi Guo
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """               
        
        def dfs(k, n, combo):            
            if k * n == 0:
                if k + n == 0:
                    self.res.append(combo[1:])
            else:
                for num in range(combo[-1]+1,min(n+1,10)):
                    dfs(k-1, n-num, combo + [num])
                    
        self.res = []            
        dfs(k, n, [0])
        return self.res

k = 3
n = 9 
test = Solution()
print(test.combinationSum3(k, n))