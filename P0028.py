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
        
        # length of two strings
        lh = len(haystack)
        ln = len(needle)
        
        # deal with trivial cases
        if (ln == 0):            
            return 0            
        if (lh < ln):   
            return -1
        
        # start searching from start
        p = 0
        # stop when remaining substring not long enough        
        while p <= lh-ln:            
            # find next position of the first character
            # in the remaining substring
            pp = haystack[p:].find(needle[0])
            # if first character exists in remaining substring
            # and remaining substring long enough
            if (pp != -1) and (p+pp+ln <= lh):
                # check if target is found
                if haystack[p+pp:p+pp+ln] == needle:
                    # return current position
                    return p + pp
                else:
                    # if not found update starting position
                    # as the one after current position of found first character
                    p = p + pp + 1
            else: 
                # if first character does not exist in remaining substring
                # return -1
                return -1
        
        # return default result (not found)
        return -1
                
        
haystack = "a"
needle = "a"   

test = Solution()
p = test.strStr(haystack, needle)
print(p)         