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
        
        # length of string
        sl = len(s)
        # set for position a indicates a Palindrome (a, b)
        self.isPalindrome = defaultdict(set)       
        
        # find all substrings that are palindromes
        for c in xrange(sl):            
            
            # palindromes of odd lengths
            # half length of palindromes
            l = 0  
            # starting from current position, try to validate symmetry on both sides
            while 0 <= c - l and c + l <= sl - 1 and s[c - l] == s[c + l]:
                # if a palindrome is found, add the end position to the set of starting position                
                self.isPalindrome[c - l].add(c + l)
                # increase half length and check next characters
                l += 1
            
            # palindromes of even lengths
            # half length of palindromes
            l = 0
            # starting from current position, try to validate symmetry on both sides
            while 0 <= c - l and c + l + 1 <= sl -1 and s[c - l] == s[c + l + 1]:
                # if a palindrome is found, add the end position to the set of starting position
                self.isPalindrome[c - l].add(c + l + 1)
                # increase half length and check next characters
                l += 1        
        
        # all palindrome combinations
        self.ans = []       
        # dfs from starting character to search for paths to ending character
        def dfs(p, combo):          
            # if the ending character is reached, the whole string is partitioned as palindromes
            if p == sl:
                # add current combo to answer
                self.ans.append(combo) 
            # if the ending character has not been reached, continue searching for paths
            else:
                # jump to one of the end points in the set for current position
                # i.e. try all viable routes
                for pp in self.isPalindrome[p]:
                    # continue dfs with updated combination of palindromes
                    dfs(pp + 1, combo + [s[p:pp+1]])
        
        # start dfs from beginning
        dfs(0,[])  
        # return all palindrome combinations         
        return self.ans          

s = 'aabb'        
test = Solution()
print test.partition(s)


                
                
            