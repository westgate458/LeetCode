# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:42:13 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """        
        # dictionary if current number already appeared
        d = {}
        # continue if current number has not appeared before
        while n not in d:
            # if current number is 1, then it is happy number
            if n == 1:
                return True
            # mark current number already appeared
            d[n] = True
            # next number
            m = 0
            # digit-wise operation
            while (n):
                # add (current digit)^2 to next number
                m += (n%10) ** 2
                # move on to next digit
                n /= 10            
            # copy next number
            n = m        
        # if we got into a loop of n's
        # return not happy number
        return False



n = 99      
n = 19  
test = Solution()
print test.isHappy(n)