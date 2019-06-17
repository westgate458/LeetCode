# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:25:58 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d1, d2 = {}, {}        
        for i in xrange(len(s)-9):
            if s[i:i+10] not in d1:
                d1[s[i:i+10]] = True
            else:                    
                d2[s[i:i+10]] = True 
        ans = d2.keys()        
        return ans

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
test = Solution()
print test.findRepeatedDnaSequences(s)