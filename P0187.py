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
        # dictionary 1: if have seen once
        # dictionary 2: if have seen more than once
        d1, d2 = {}, {}        
        # check each 10-character subspring
        for i in xrange(len(s)-9):
            # if we have not seen this one
            if s[i:i+10] not in d1:
                # mark we have seen this once
                d1[s[i:i+10]] = True
            # if we have seen this one once
            else:                    
                # mark we have seen it more than once
                d2[s[i:i+10]] = True 
        # return all substrings that appear more than once      
        return d2.keys()                

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
test = Solution()
print test.findRepeatedDnaSequences(s)