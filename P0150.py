# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:59:58 2019

@author: Tianqi Guo
"""
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        operations = set(['+', '-', '*', '/'])
        
        s = []
        
        for token in tokens:
            if token in operations:
                num2 = s.pop()
                num1 = s.pop()
                if token == '+':
                    num = num1 + num2
                elif token == '-':
                    num = num1 - num2
                elif token == '*':
                    num = num1 * num2
                else:
                    num = num1 / num2
            else:
                num = float(token)
            if num > 0:
                num = math.floor(num)
            else:
                num = math.ceil(num)
            s.append(num)            
        
        return int(s[0])
        

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
test = Solution()
print test.evalRPN(tokens)