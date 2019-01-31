# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:06:23 2019

@author: Tianqi Guo
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Solution 1: add a and b digit by digit
        # length of two numbers
        l1 = len(a)
        l2 = len(b)
        
        # pad the shorter number with leading zeros
        if l1 > l2:
            l = l1
            b = '0' * (l1 - l2) + b
        else:
            l = l2
            a = '0' * (l2 - l1) + a
            
        # carry = 1 if the sum of current digtis >= 2
        carry = 0
        # answer string
        ans = ''
        # add two numbers digit by digit
        for i in range(l):
            # update the sum and carry for current digit
            carry, sm = divmod(int(a[-1-i]) + int(b[-1-i]) + carry , 2) 
            # update the answer string for current digit
            ans = ans + str(sm)   
        
        # if carry = 1 after all digits are added
        if carry == 1:
            # update the answer string
            ans = ans + str(carry)
        
        # return answer string in reversed order
        return ans[::-1]
    
        # Solution 2: add two numbers as binary, and format sum as binary
        # return format(int(a,2) + int(b,2),'b')

a = '1'
b = '101'
test = Solution()
print(test.addBinary(a,b))
    
    