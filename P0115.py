# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:55:05 2019

@author: Tianqi Guo
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """        
        
        # Solution 1
        l1, l2 = len(s), len(t)        
        f = [[0] * (l2 + 1) for n in range(l1+1)]
        f[0][0] = 1        
        for i in range(l1):
            f[i+1][0] = 1
            for j in range(l2):
                f[i+1][j+1] = f[i][j+1]
                if s[i] == t[j]:
                    f[i+1][j+1] = f[i+1][j+1] + f[i][j]
        return f[-1][-1]
        
        # Solution 2
        f = [1] + [0] * len(t)               
        for i in range(len(s)):                     
            for j in range(len(t)-1,-1,-1):                
                if s[i] == t[j]: f[j+1] += f[j]        
        return f[-1]

s = "rabbbit"
t = "rabbit"

test = Solution()
print test.numDistinct(s, t)
        