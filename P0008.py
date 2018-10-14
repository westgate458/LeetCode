# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:48:17 2018

@author: Tianqi Guo
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """       
        
        l = len(str)
        # initialization
        n = 0.0
        # string of number characters
        nc = "0123456789"
        # sign equal 1 if positive, -1 if negative
        sign = 1
        # flag if number has started
        num_start = False
        # check each character in string one by one
        for i in range(l):            
            c = str[i]
            # whitespace characters before number starts
            if (c == " ") and (not num_start):
                continue
            # encounter negative sign
            if (c == "-") and (not num_start):
                # start number and set sign to negative
                sign = -1
                num_start = 1
                continue
            # encounter positive sign
            if (c == "+") and (not num_start):
                # start number and set sign to positive
                sign = 1
                num_start = 1
                continue
            # find current digit in the number character string
            digit = nc.find(c)
            # if current digit is number
            if digit != -1:
                # start number and update result
                num_start = 1
                n = n * 10 + digit
            else:
                # if current digit is not number
                # illegal expression encountered, exit search
                break
        # sign correction
        n = int(n * sign)
        # check if number exceeds range
        n = max(n, -2**31)
        n = min(n, 2**31 - 1)
        
        # return result
        return(n)
        
str = "+ 2a-2"
test = Solution()
print(test.myAtoi(str))
