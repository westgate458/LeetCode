# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:52:51 2019

@author: Tianqi Guo
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 0:
            return 0
        
        nn, power, k, ans = n, 1, 0, 0 
        
        while nn:            
            num = nn%10
            nn //= 10             
            ans += num * k + (num > 1) * power + (num == 1) * (n % power + 1)
            k = 10*k + power    
            power *= 10
            
        return ans
        
n = 13
test = Solution()
print(test.countDigitOne(n))
        