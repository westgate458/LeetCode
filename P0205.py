# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:02:06 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1: without sorting  
        # ds: for each character in s, what should it be replaced with to match t
        # dt: for each character in t, has it been mapped from s
        ds, dt = {}, {}        
        # check each character in s
        for i, c in enumerate(s):
            # if current character in s has appeared before
            if c in ds:
                # if current character in t is not
                # the documented replacement for current character in s
                if t[i] != ds[c]:
                    # 1-to-1 mapping not feasible, s and t not isomorphic
                    return False
            # if it is the first appearance of the current character in s 
            # but the current character in t has already been mapped to another character in s 
            elif t[i] in dt:
                # 1-to-1 mapping not feasible, s and t not isomorphic                
                return False
            # if it is the first appearance of the current character in s 
            # and it is the first appearance of the current character in t              
            else:
                # record current mapping in ds and dt
                ds[c] = t[i]
                dt[t[i]] = True
        # if no conflicts have been found
        # mapping is feasible, s and t are isomorphic
        return True
        
#        # Solution 2: from sorting
#        from collections import defaultdict
#        ds = defaultdict(list)
#        dt = defaultdict(list)        
#        for i in xrange(len(s)):
#            ds[s[i]] += [i]
#            dt[t[i]] += [i]           
#        return sorted(ds.values()) == sorted(dt.values())
        
s = "egg"
t = "add"

s = "foo"
t = "bar"

s = "ab"
t = "aa"

s = "paper"
t = "title"  

test = Solution()
print test.isIsomorphic(s, t)
       