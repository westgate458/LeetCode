# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:24:01 2018

@author: Tianqi Guo
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = len(s)
        # length of longest string
        m = 1
        # start position of longest string
        p = 0
        # if from i to j in s is Palindromic
        TF = [[False] * l for i in range(l)]
        # each 1-length substring is Palindromic
        for i in range(l):
            TF[i][i] = True
        # each 2-length substring is Palindromic
        # if both characters are the same
        for i in range(l-1):
            TF[i][i+1] = (s[i] == s[i+1])
            # update length and pointer
            if TF[i][i+1]:
                m = 2
                p = i
        # check all substrings of m_ij-character long
        # if they are Palindromic using results of shorter substrings
        for m_ij in range(3,l + 1):    
            # all substrings of m_ij-character long
            for i in range(0,l - m_ij + 1):
                # check if the first and last characters are the same
                j = i + m_ij - 1
                # Palindromic if two characters are the same 
                # and substring in the middle is Palindromic
                TF[i][j] = (s[i] == s[j]) and TF[i+1][j-1]      
                # update length and pointer
                if TF[i][j]:
                    m_ij = j - i + 1
                    if m_ij > m:
                        m = m_ij
                        p = i               
        
        # return result
        return(s[p:p+m])
        
s = "cbbd"       
test = Solution()                
print(test.longestPalindrome(s))
 
        