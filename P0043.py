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
        
        if (num1 == '0') or (num2 == '0'):
            return '0'
        
        l1 = len(num1)
        l2 = len(num2)

        digits = "0123456789"

        n1 = []
        n2 = []

        for i in range(l1):
            d = digits.find(num1[l1-1-i])
            if d > 0:
                n1.append([d,i])

        for i in range(l2):
            d = digits.find(num2[l2-1-i])
            if d > 0:
                n2.append([d,i])

        ans = [0 for x in range(l1+l2)]

        for d1,i in n1:
            for d2,j in n2:
                ans[i+j] = ans[i+j] + d1 * d2    

        s = ""
        carry = 0
        for x in ans:
            temp = carry + x
            s = str(temp%10) + s
            carry = temp / 10
            
        return s.lstrip('0') 

num1 = "123"
num2 = "456"        
test = Solution()
print(test.multiply(num1,num2))        