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
        # Solution 1        
        ds, dt = {}, {}        
        for i, c in enumerate(s):
            if c in ds:
                if t[i] != ds[c]:
                    return False
            elif t[i] in dt:
                return False
            else:
                ds[c] = t[i]
                dt[t[i]] = True
        return True
        
#        # Solution 2
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
       