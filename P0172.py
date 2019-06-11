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
        
        ans = 0
        while (n):
            n /= 5
            ans += n         
            
        return ans

n = 200

test = Solution()
print test.trailingZeroes(n)