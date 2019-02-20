# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 22:35:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # length of the string
        n = len(t)
        # string for minimum window
        ss = ''
        # minimum length of the window
        m_l = float('inf')   
        
        # hash dictionary 
        # stores the times of occurrence of each character
        count = {}                
        # count the occurrence of each character
        for i in range(n):
            # a new character is found
            if not t[i] in count:
                # set its occurence to 1
                count[t[i]] = 1
            # an old character occurred again
            else:
                # update its counting
                count[t[i]] = count[t[i]] + 1   
        
        # pointer of the window start position
        p0 = 0
        
        # pointer of the window ending position
        for i in range(len(s)):
            
            # if current character is in t
            if s[i] in t:  
                
                # reduce its remaining counting by 1
                # negative value means it has appeared more times
                # than needed in t
                count[s[i]] = count[s[i]] - 1
                
                # if current character has not appeared
                # for requred times in the current window
                if count[s[i]] >= 0:
                    # when current character is included in the window
                    # the number of required characters is reduced by 1
                    n = n - 1
                
                # update the start pointer
                # move it towards tail if 
                # 1) the starting character is not a required one
                # 2) the starting character is a required one, and 
                #    it has appeared more times than needed
                while (not (s[p0] in t)) or (count[s[p0]] + 1 <= 0):            
                    # if it is the 2nd scenario
                    if s[p0] in t:
                        # increase the remaining counting by 1
                        # since moving pointer makes current character
                        # out from the current window
                        count[s[p0]] = count[s[p0]] + 1
                    # move the start pointer by 1
                    # slide the window towards right
                    p0 = p0 + 1
                
                # if all characters have appeared at least required times
                # and the current window length is smaller
                if (n == 0) and (i - p0 + 1 < m_l):
                    # update the answer window string
                    ss = s[p0:i+1]
                    # update the window length
                    m_l = i - p0 + 1 
        
        # return answer window string
        return ss    
   
s = "ADOBECODEBANC"
t = "ABC"            
test = Solution()
print test.minWindow(s, t)
            
        
        
        
    