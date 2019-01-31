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
        
        # carry one if sum of current digit >= 10
        carry = 1
        # length of the number
        d = len(digits) - 1
        # continue summation if carry = 1
        # start from the right most digit (last in the list)
        while (carry > 0) and (d >= 0):
            # update current digit and the carry
            carry, digits[d] = divmod(digits[d] + carry, 10)
            # move to next digit
            d = d - 1
        
        # if carry = 1 after all digits are added
        if carry > 0:
            # insert a new digit before the starting digit
            digits.insert(0,carry)
        
        # return the number after adding one
        return digits
        
digits = [9]
test = Solution()
print test.plusOne(digits)