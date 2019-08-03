# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:53:15 2019

@author: Tianqi Guo
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Solution 1 beats 99%: only stack for sign and res
        # initialize final result, current sign, current number, and ord of character 0
        res, sign, temp, ord0 = 0, 1, 0, ord('0')
        # stacks for signs and intermidiate results to deal with ()
        sgn_stack = []
        rst_stack = []
        
        # check each character
        for c in s:   
            # if current character is a number
            if c.isdigit():
                # update current number
                temp = temp*10 + ord(c) - ord0
            # if current character is an operation sign or ' '
            # it means a number is finished
            else:
                # update result with sign and number
                res += sign * temp
                # reset current number
                temp = 0
                # deal with operation signs
                # if we ran into a left bracket
                if c == '(':                
                    # intermidiate results and current sign need to be stacked
                    # so we can deal with operations inside () first
                    rst_stack.append(res)
                    sgn_stack.append(sign)
                    # reset result
                    res = 0 
                # if a () session has ended
                elif c == ')':
                    # treating results inside () as a single number
                    # and incorporate it into previous results
                    res = rst_stack.pop(-1) + sgn_stack.pop(-1) * res 
                
                # update the current sign                     
                if c == '-':
                    sign = -1
                else:
                    sign = 1
                
        # update final results with the last number and its sign        
        return res + sign * temp
                
        
        
        # Solution 2 beats 38.6%: stack for all
#        ss = [0]        
#        current = ''  
#        
#        for c in '('+s+')':
#           
#            if c in [' ', '+', '-','(',')']:
#                if current:    
#                    num = int(current)
#                    if ss[-1] == '-':
#                        ss.pop(-1)
#                        num = -num
#                    if ss[-1] != '(':
#                        ss[-1] += num
#                    else:
#                        ss.append(num)
#                    current = ''
#                if c == ')':
#                    num = ss.pop(-1)                                          
#                    ss.pop(-1)                   
#                    if ss[-1] == '-':
#                        ss.pop(-1)
#                        num = -num
#                    if ss[-1] != '(':
#                        ss[-1] += num
#                    else:
#                        ss.append(num)
#                if c in ['-', '(']:                     
#                    ss.append(c)
#            else:
#                current += c        
#        
#        return ss[-1]


s = "1-(1+1)"

s= " 2-1 + 2 "

s = "(1+(4+5+2)-3)+(6+8)"

test = Solution()
print(test.calculate(s))
                
                    
    