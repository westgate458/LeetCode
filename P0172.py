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
        # to have trailing zero, there must be production of factors 2 and 5
        # we only need to count how many 5's in total in the factorial
        # since there are more factor 2 than factor 5
        # n! = n * (n-1) * (n-2) * ... * 1
        # from 1 to n,
        # 1) every 5th (5^1) element has a factor of 5
        # 2) every 25th (5^2) element has an additional factor of 5
        # ...
        # i) every 5^i element has an additional factor of 5
        # to sum all those numbers of 5 up we have
        # ans = n/5^1 + n/5^2 + n/5^3 + ... + n/5^i (*)
        
        # total number of 5's
        ans = 0
        # calculate the summation of the sequence (*)
        # continue dividing n by 5 until there is no more 5's
        while (n):
            # how many additional 5's in this term from (*)
            n /= 5
            # update total number
            ans += n         
        
        # return the number of trailing 0's
        return ans

n = 200

test = Solution()
print test.trailingZeroes(n)