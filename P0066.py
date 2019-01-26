# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:10:00 2019

@author: Tianqi Guo
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        d = len(digits) - 1
        while (carry > 0) and (d >= 0):
            carry, digits[d] = divmod(digits[d] + carry, 10)
            d = d - 1

        if carry > 0:
            digits.insert(0,carry)
        return digits
        
digits = [9]
test = Solution()
print test.plusOne(digits)