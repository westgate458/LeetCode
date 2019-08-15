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
        # deal with trivial case
        if n <= 0:
            return 0
        # initialize the following
        # nn: current number
        # power: 10^(iteration)
        # k: number of 1's in 1*10^iteration (1~10, 1~100, 1~1000, etc)
        # ans: number of ones
        nn, power, k, ans = n, 1, 0, 0 
        
        # continue loop until all digits are checked
        # e.g. original n is 4321, now nn is 43
        while nn:            
            # current last digit, e.g. 43 -> 3
            num = nn%10
            # update current number, e.g. 43 -> 4
            nn //= 10             
            # update answer with three parts
            # 1) num * k: number of 1's in 1 ~ num*10^iteration (e.g. 3 * (1~100))
            # 2) if num>1, then there are extra power * 1's at current digit (e.g. 100 * 1's from 100 ~ 199)
            # 3) if num=1, then there are only reduced extra one's (e.g. for 123, only 24 ones from 100 to 123)
            ans += num * k + (num > 1) * power + (num == 1) * (n % power + 1)
            # update k and power
            k = 10*k + power    
            power *= 10
        
        # return number of one's            
        return ans
        
n = 13
test = Solution()
print(test.countDigitOne(n))
        