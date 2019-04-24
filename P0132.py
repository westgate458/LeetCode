# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:40:13 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        if s == s[::-1]:
            return 0
        
        sl = len(s)
        for c in xrange(sl):           
            if s[:c+1] == s[:c+1][::-1] and s[c+1:] == s[c+1:][::-1]:
                return 1
        
        cuts = [x for x in xrange(-1,sl)]

        for c in xrange(sl):            
            l = 0  
            while 0 <= c - l and c + l < sl and s[c - l] == s[c + l]:
                cuts[c+l+1] = min(cuts[c+l+1], cuts[c-l] + 1)
                l += 1
            l = 0
            while 0 <= c - l and c + l + 1 < sl and s[c - l] == s[c + l + 1]:
                cuts[c+l+2] = min(cuts[c+l+2], cuts[c-l] + 1)                
                l += 1             
                    
        return cuts[-1]          

s = 'aabb'        
test = Solution()
print test.minCut(s)