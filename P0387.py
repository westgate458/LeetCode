# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:20:37 2019

@author: Tianqi Guo
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1 beats 99.94%: rfind
        ans = float('inf')
        for c in string.ascii_lowercase:
            ind = s.find(c)
            if ind != -1 and s.rfind(c) == ind:
                ans = min(ans, ind)
        return -1 if ans == float('inf') else ans
    
        # Solution 2 beats 61.94%: dictionary
        from collections import defaultdict
        d = defaultdict(list)
        for i,c in enumerate(s):
            d[c] += [i] 
        d = [d[c][0] for c in d if len(d[c])==1]
        return min(d) if d else -1