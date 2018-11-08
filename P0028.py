# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:30:22 2018

@author: Tianqi Guo
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        if (ln == 0):            
            return 0
            
        if (lh < ln):   
            return -1
        
        p = 0
        while p <= lh-ln:            
            pp = haystack[p:].find(needle[0])
            if (pp != -1) and (p+pp+ln <= lh):
                if haystack[p+pp:p+pp+ln] == needle:
                    return p + pp
                else:
                    p = p + pp + 1
            else:                
                return -1
        return -1
                
        
haystack = "a"
needle = "a"   

test = Solution()
p = test.strStr(haystack, needle)
print(p)         