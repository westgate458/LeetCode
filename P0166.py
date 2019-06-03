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
        
        if numerator == 0:
            return '0'
        elif numerator * denominator < 0:
            ans = '-'               
            numerator, denominator = abs(numerator), abs(denominator)
        else:
            ans = ''   
        
        digits, numerators = [], [0]   
        
        while numerator not in numerators:
            numerators.append(numerator)
            digits.append(numerator//denominator)
            numerator = (numerator%denominator) * 10   

        ans += str(digits[0])
        l0 = len(ans)
        if len(digits) > 1:
            ans = ans + '.' + ''.join([str(digit) for digit in digits[1:]])
            if numerator != 0:                   
                pos = l0 + numerators.index(numerator) - 1
                ans = ans[:pos] + '(' + ans[pos:] + ')'         

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