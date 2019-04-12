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
        
        # Solution 1: complete version, space complexity O(mn)        
        # length of two strings
        l1, l2 = len(s), len(t)  
        # state function O(mn)
        f = [[0] * (l2 + 1) for n in range(l1+1)]
        # empty string matches empty string
        f[0][0] = 1      
        
        # solve sub problems
        # iterate over length of s
        for i in range(l1):
            # if target t is empty, remove all characters from s to match
            f[i+1][0] = 1
            # iterate over length of t
            for j in range(l2):
                # number of ways to match for f[i+1][j+1]
                # is at least the number of ways for f[i][j+1]
                # i.e. when character s[i] is not used in matching
                f[i+1][j+1] = f[i][j+1]
                # if s[i] matches t[j]
                if s[i] == t[j]:
                    # then there are two ways to reach current state:
                    # 1) character s[i] is not used in matching, state from f[i][j+1]
                    # 2) characters s[i] and t[j] are used, state from f[i][j]
                    # sum them up
                    f[i+1][j+1] = f[i+1][j+1] + f[i][j]
        
        # the last state is the total number of ways
        return f[-1][-1]
        
        # Solution 2: simplified version, space complexity O(n)        
        # empty matches empty, others initialized by 0
        f = [1] + [0] * len(t)               
        # iterate over length of s
        for i in range(len(s)):           
            # iterate over length of t, but in reversed order
            # since f[i+1][j+1] depends only on previous elements
            # update the last elements first
            for j in range(len(t)-1,-1,-1): 
                # f[i+1][j+1] is now natually f[i][j+1]
                # only update it when characters match
                if s[i] == t[j]: f[j+1] += f[j]       
        # the last state is the total number of ways
        return f[-1]

s = "rabbbit"
t = "rabbit"

test = Solution()
print test.numDistinct(s, t)
        