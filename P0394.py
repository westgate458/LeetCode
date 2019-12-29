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
        # stack for previous status before current brackets
        stack = []
        # ss: decoded string
        # nn: number before the bracket
        ss, nn = '', ''
        # check each character
        for c in s:
            # if current character is abc
            if c.isalpha():
                # add it to decoded string
                ss += c
            # if current character is number
            elif c.isdigit():
                # update number
                nn += c
            # if current character is '['
            elif c == '[':
                # push current state to the stack
                stack.append((ss, nn))
                # start new string and number
                ss, nn = '', ''
            # if current character is ']'                
            else:
                # retrieve previous status
                pre_ss, pre_nn = stack.pop()
                # decode the string in [] and add it to previous string
                ss = pre_ss + int(pre_nn) * ss
        # return decoded string
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