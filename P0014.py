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
        
        # deal with empty string sets
        if (not strs) or (n == 0):
            return ''
        
        # deal with the situation if the shortest string in set is empty
        min_len = len(strs[0])
        for i in range(n):
            min_len = min(min_len,len(strs[i]))
        if min_len == 0:
            return ''
        
        # set initial maximum length to 0
        l = 0        
        # flag if a mismatch is found
        flag = False
        # the maximum length can't exceed 
        # the length of the shortest string in set
        for l in range(min_len):     
            # compare the l-th character in each string
            for i in range(0,n):
                # if a mistach is found                
                if (strs[0][l] != strs[i][l]):
                    # update the flag and terminate searching
                    flag = True
                    break
            # if a mistach is found, terminate searching
            # the maximum length is then l
            if flag:
                break
            
        # if the entire searching is completed
        # and no mismatch has been found
        if not flag:
            # the maximum length is then l + 1
            l = l + 1
        
        # return the longest common prefix substring
        return strs[0][0:l]        
        
s = ["abab","aba",""]
test = Solution()
print(test.longestCommonPrefix(s)) 