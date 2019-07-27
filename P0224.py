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
        
        ss = [0]        
        current = ''  
        
        for c in '('+s+')':
           
            if c in [' ', '+', '-','(',')']:
                if current:    
                    num = int(current)
                    if ss[-1] == '-':
                        ss.pop(-1)
                        num = -num
                    if ss[-1] != '(':
                        ss[-1] += num
                    else:
                        ss.append(num)
                    current = ''
                if c == ')':
                    num = ss.pop(-1)                                          
                    ss.pop(-1)                   
                    if ss[-1] == '-':
                        ss.pop(-1)
                        num = -num
                    if ss[-1] != '(':
                        ss[-1] += num
                    else:
                        ss.append(num)
                if c in ['-', '(']:                     
                    ss.append(c)
            else:
                current += c        
        
        return ss[-1]

s= " 2-1 + 2 "
s = "1-(1+1)"
s = "(1+(4+5+2)-3)+(6+8)"

test = Solution()
print(test.calculate(s))
                
                    
    