# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:00:47 2018

@author: Tianqi Guo
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """  
       
        n = len(strs)
        if (not strs) or (n == 0):
            return ''
        
        min_len = len(strs[0])
        for i in range(n):
            min_len = min(min_len,len(strs[i]))
        if min_len == 0:
            return ''
        
        l = 0        
        flag = False
        for l in range(min_len):           
            for i in range(0,n):
                if (strs[0][l] != strs[i][l]):
                    flag = True
                    break          
            if flag:
                break
        if not flag:
            l = l + 1
        return strs[0][0:l]        
        
s = ["abab","aba",""]
test = Solution()
print(test.longestCommonPrefix(s)) 