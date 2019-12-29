# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:46:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the dictionary for dp
        self.d = {1:0}        
        # function to solve subproblems
        def replace(n):            
            # if current problem has not been solved
            if n not in self.d:
                # if current number is even
                if n%2 == 0:
                    # minimum operation is from its half
                    self.d[n] = replace(n/2) + 1
                # if current number is odd
                else:
                    # then choose from its two neighbors
                    self.d[n] = min(replace(n+1), replace(n-1)) + 1
            # return the minimum operations for current number
            return self.d[n]        
        # call the subfunction and solve from top-down
        return replace(n)