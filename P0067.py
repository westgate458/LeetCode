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
        l1 = len(a)
        l2 = len(b)

        if l1 > l2:
            l = l1
            b = '0' * (l1 - l2) + b
        else:
            l = l2
            a = '0' * (l2 - l1) + a

        carry = 0;
        ans = ''
        for i in range(l):
            carry, sm = divmod(int(a[-1-i]) + int(b[-1-i]) + carry , 2)   
            ans = ans + str(sm)   

        if carry == 1:
            ans = ans + str(carry)

        return ans[::-1]
    
#        return format(int(a,2) + int(b,2),'b')


a = '1'
b = '101'
test = Solution()
print(test.addBinary(a,b))
    
    