# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:06:12 2018

@author: Tianqi Guo
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # length of two strings
        ls = len(s)
        lp = len(p)
        # initialization of match flag
        # match[i][j] is true if substring of first i characters from s
        # matches the substring of first j characters from p
        match = [[False] * (lp+1) for i in range(ls+1)]
        # empty string matches itself
        match[0][0] = True
        # empty string matches substring from p 
        # if the latter only consists of character+*
        for j in range(1,lp+1):
            c_p = p[j-1]
            if c_p == '*':
                match[0][j] = match[0][j-2]   
                
        # check all substring from s and p to see if they match
        # three senarios lead to the matching
        # 1) two current characters the same, and preceeding substrings match
        # 2) current substring from s matches preceeding substring from p before *
        # 3) current substring from p before * matches preceeding substring from s
        for i in range(1,ls+1):
            for j in range(1,lp+1):
                # check if the last characters match
                c_s = s[i-1]
                c_p = p[j-1]
                c_match = (c_p == '.') or (c_s == c_p);
                # current two substring matches if
                # last characters match, 
                # and preceeding substrings match
                if c_match and match[i-1][j-1]:
                    match[i][j] = True
                    continue        
                # if current character if p is *
                if c_p == '*':
                    # current two current substrings match if
                    # the current substring in s matches 
                    # the preceeding substring in p 
                    # and character before * is repeated 0 times
                    if match[i][j-2]:
                        match[i][j] = True
                        continue      
                    # check if the character before current * in p matches 
                    # the current character in s
                    c_pp = p[j-2]                    
                    c_match = (c_pp == '.') or (c_s == c_pp);
                    # the two current substrings match if
                    # two characters match
                    # and the preceeding substring in s matches 
                    # the current substring in p
                    if c_match and match[i-1][j]:
                        match[i][j] = True
                        continue
                # if all three matching senarios don't occur
                # the current two substrins don't match
        
        # return the last match flag
        # which corresponds to the two entire strings
        return(match[-1][-1])
  
s = "ab"
p = ".*"       
test = Solution()
print(test.isMatch(s,p))    
        
        
        
        