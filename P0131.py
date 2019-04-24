# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:33:52 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        sl = len(s)
        self.isPalindrome = defaultdict(set)       
        
        for c in xrange(sl):            
            l = 0  
            while 0 <= c - l and c + l <= sl - 1 and s[c - l] == s[c + l]:
                self.isPalindrome[c - l].add(c + l)
                l += 1
            l = 0
            while 0 <= c - l and c + l + 1 <= sl -1 and s[c - l] == s[c + l + 1]:
                self.isPalindrome[c - l].add(c + l + 1)
                l += 1        
        
        self.ans = []        
        def dfs(p, combo):            
            if p == sl:
                self.ans.append(combo) 
            else:
                for pp in self.isPalindrome[p]:
                    dfs(pp + 1, combo + [s[p:pp+1]])
        
        dfs(0,[])            
        return self.ans
          

s = 'aabb'        
test = Solution()
print test.partition(s)


                
                
            