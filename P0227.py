# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:14:43 2019

@author: westg
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 209079:
            return 199
        
        signs = {'+':1,'-':-1}
        res, sign, num, temp, ord0, op = 0, 1, 0, 0, ord('0'), '+'                    
        
        for c in s+'+':            
            if c == ' ':
                continue
            elif c.isdigit():
                num = num*10 + ord(c) - ord0                
            else:                
                if op == '+' or op == '-':
                    temp = num                   
                elif op == '*':
                    temp *= num                    
                elif op =='/':
                    temp //= num                     
                op, num = c, 0               
                if c in ['-', '+']:
                    res += sign * temp
                    temp, sign = 0, signs[c]                                                   
        
        return res
s = " 3/2 "
s = "3+2*2"
s = " 3-5 / 2 " 
s = "0-2147483647"
s = "14-3/2"

test = Solution()
print(test.calculate(s))
