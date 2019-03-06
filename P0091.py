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
        
        if s[0] == '0':
            return 0            
        
        l = len(s)
        ans = [0] * (l+1)
        ans[0:2] = [1,1]       
        
        for c in range(1,l):     
            
            if s[c:c+1] > '0':
                ans[c+1] = ans[c]           
            if s[c-1:c+1] == '00':
                break
            if s[c-1] =='1' or (s[c-1] =='2' and s[c] < '7'):
                ans[c+1] = ans[c+1] + ans[c-1]
            
        return ans[-1]
    
    
s = '101'
test = Solution()
print test.numDecodings(s)
            