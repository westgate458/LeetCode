# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:34:11 2018

@author: Tianqi Guo
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        
        l = len(s)
        m = min(1,l)
        # last position of each appearing character
        lst_pos = {}
        # current string starting position
        current_s = 0
        for i in range(l):
            c = s[i]    
            # if current character has never appeared before
            if not c in lst_pos:
                # update dictionary
                lst_pos.update({c:i})
            else:
                # if current character has appeared
                # fectch last position
                lp_c = lst_pos[c]
                # if current character appeared already 
                # in current string
                if lp_c >= current_s:
                    # current string comes to an end
                    # update the length of the longest string
                    m = max(i - current_s, m)   
                    # start new string after last appearance position
                    current_s = lp_c + 1
                # current position is the last appearance position
                # of the current character
                lst_pos.update({c:i})
        # check if the last string is the longest
        if l > 0:
            m = max(i - current_s + 1, m)     
        # return longest length
        return(m)    
        
s =   "abcabcbb"          
test = Solution()
print(test.lengthOfLongestSubstring(s))        
 
  
        
        
        
        