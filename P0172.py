# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:57:03 2019

@author: Tianqi Guo
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        tens = n // 10
        ones = n % 10        
               
        ans = tens * 2
        if ones >= 5:
            ans += 1
        return ans

n = 5
test = Solution()
print test.trailingZeroes(n)