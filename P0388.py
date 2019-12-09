# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:55:17 2019

@author: Tianqi Guo
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        ans, s, l = 0, [], [-1]      
        
        for path in input.split("\n"):
            level = path.count('\t')
            while level <= l[-1]:
                l.pop()
                s.pop()
            s.append(path.lstrip('\t'))
            l.append(level)
            if '.' in path:                
                ans = max(ans, len('/'.join(s)))
        return(ans)