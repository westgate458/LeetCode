# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:30:15 2019

@author: Tianqi Guo
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # deal with trivial case
        if numerator == 0:
            return '0'
        # check signs of the two number
        elif numerator * denominator < 0:
            # negative result
            ans = '-'        
            # take absolute values
            numerator, denominator = abs(numerator), abs(denominator)
        else:
            # positive result
            ans = ''   
        
        # list of current digit, and current numerator
        digits, numerators = [], [0]   
        
        # if current numerator has not been encountered before
        # i.e. the fractional part is not repeating yet
        while numerator not in numerators:
            # keep record of current numerator
            numerators.append(numerator)
            # calculate current digit for the decimal
            digits.append(numerator//denominator)
            # update the numerator
            numerator = (numerator%denominator) * 10   
        
        # copy the integer part first
        ans += str(digits[0])
        # length of the answer string so far
        l0 = len(ans)
        # if there is fractional part
        if len(digits) > 1:
            # update answer string with '.' and other digits for the decimal part
            ans = ans + '.' + ''.join([str(digit) for digit in digits[1:]])
            # if the final numerator is not zero
            # i.e. the decimal part is repeating
            if numerator != 0:                  
                # the last encounter of current numerator is where the repeating starts
                pos = l0 + numerators.index(numerator) - 1
                # enclose the repeating part in parentheses
                ans = ans[:pos] + '(' + ans[pos:] + ')'         
        
        # return answer string
        return ans
    

numerator = 1
denominator = 2   

numerator = 2
denominator = 1   

numerator = 1
denominator = 7 

numerator = 2
denominator = 3 

numerator = -50
denominator = 8 

test = Solution()
print test.fractionToDecimal(numerator, denominator)