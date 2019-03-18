# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:50:09 2019

@author: Tianqi Guo
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # deal with trivial case
        if s[0] == '0':
            return 0            
        
        # length of string
        l = len(s)
        # number of ways to decode each substring
        ans = [0] * (l+1)
        # only one way for empty string and first character
        ans[0:2] = [1,1]       
        
        # for each substring
        for c in range(1,l):     
            
            # if current digit is not 0
            if s[c:c+1] > '0':
                # current substring has at least the same number of ways to decode
                # as previous substring
                ans[c+1] = ans[c]      
            # if two successive zeros are found
            if s[c-1:c+1] == '00':
                # illegal expression, no way to decode
                break
            # if most recent two digits can be decoded as one character
            if s[c-1] =='1' or (s[c-1] =='2' and s[c] < '7'):
                # current substring can be decoded two different ways
                ans[c+1] = ans[c+1] + ans[c-1]
            
        # total number of ways to decode current string
        return ans[-1]    
    
s = '101'
test = Solution()
print test.numDecodings(s)
            