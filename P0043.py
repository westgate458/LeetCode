# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:34:34 2018

@author: Tianqi Guo
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        # deal with trivial cases
        if (num1 == '0') or (num2 == '0'):
            return '0'
        
        # number of the digits
        l1 = len(num1)
        l2 = len(num2)

        # digits for fast conversion
        digits = "0123456789"
        
        # convert each string to number by digits
        n1 = []
        n2 = []
        
        # for each digit in the string
        # starting from the most right digit
        for i in range(l1):
            # convert it to number
            d = digits.find(num1[l1-1-i])
            # discard 0 digits to improve efficiency
            if d > 0:
                # record the number and its position i in terms of 10^i
                n1.append([d,i])
        
        # the same goes for the other string
        for i in range(l2):
            d = digits.find(num2[l2-1-i])
            if d > 0:
                n2.append([d,i])
        
        # ans array stores the product of each combination of digits from two numbers
        # i-th element is the product for position 10^i
        ans = [0 for x in range(l1+l2)]
        
        # for each combination (i,j) of digits from two numbers
        for d1,i in n1:
            for d2,j in n2:
                # add the product of those two digits to the answer array at position (i+j)
                ans[i+j] = ans[i+j] + d1 * d2    
        
        # answer string
        s = ""
        # carry if sum is larger than 10 at each digit
        carry = 0
        # for product x at each position 10^i in the answer array
        for x in ans:
            # sum carry and the current product
            temp = carry + x
            # add the smaller-than-10 part of summation to the answer string at i-th position for 10^i
            s = str(temp%10) + s
            # take the larger-than-10 part of summation as the carry
            carry = temp / 10
        
        # get rid of leading zeros and return the stripped answer string
        return s.lstrip('0') 

num1 = "123"
num2 = "456"        
test = Solution()
print(test.multiply(num1,num2))        