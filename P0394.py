# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:00:16 2019

@author: westg
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """    
        # Solution 1 beats 89.44%: using stack
        stack = []
        ss, nn = '', ''
        for c in s:
            if c.isalpha():
                ss += c
            elif c.isdigit():
                nn += c
            elif c == '[':
                stack.append((ss, nn))
                ss, nn = '', ''
            else:
                pre_ss, pre_nn = stack.pop()
                ss = pre_ss + int(pre_nn) * ss
        return ss
        
        # Solution 2 beats 89.44%: simple string operation
        ss = '*'
        for c in s:            
            if c != ']':
                ss += c
            else:
                p = len(ss)-1
                while ss[p] != '[':
                    p -= 1
                cc = ss[p+1:]
                p -= 1
                nn = ''
                while p >= 0 and '0' <= ss[p] <= '9':
                    nn = ss[p] + nn
                    p -= 1                
                if nn:
                    ss = ss[:p+1] + int(nn) * cc
                else:
                    ss = ss[:p+1] + cc        
        return(ss[1:])