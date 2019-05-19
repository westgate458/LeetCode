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
        # characters for operations
        operations = set(['+', '-', '*', '/'])
        # calculator stack
        s = []
        # check each token
        for token in tokens:
            # if current token is an operation
            if token in operations:
                # retrieve previous two values
                num2 = s.pop()
                num1 = s.pop()
                # perform operation accordingly
                # store result in num
                if token == '+':
                    num = num1 + num2
                elif token == '-':
                    num = num1 - num2
                elif token == '*':
                    num = num1 * num2
                else:
                    num = num1 / num2
                    # round division result towards zero
                    if num > 0:
                        num = math.floor(num)
                    else:
                        num = math.ceil(num)
            # if current token is an number
            else:
                # convert current token to float
                num = float(token)
            # place result to calculator stack
            s.append(num)            
        # return the final result still in the stack
        return int(s[0])        

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
test = Solution()
print test.evalRPN(tokens)