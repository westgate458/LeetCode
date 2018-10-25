# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:52:25 2018

@author: Tianqi Guo
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_p = "([{"        
        l = len(s)
        p = []
        for i in range(l):
            c = s[i]
            if left_p.find(c) != -1:
                p.append(c)
            else:
                if not p:
                    return False
                if c == ')':
                    if p[-1] == '(':
                        p.pop(-1)
                    else:
                        return False
                if c == ']':
                    if p[-1] == '[':
                        p.pop(-1)
                    else:
                        return False
                if c == '}':
                    if p[-1] == '{':
                        p.pop(-1)
                    else:
                        return False
        if not p:
            return True
        else:
            return False
        
s = "]"
test = Solution()
print(test.isValid(s))
    
                