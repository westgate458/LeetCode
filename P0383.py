# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:54:16 2019

@author: Tianqi Guo
"""



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """      
        # Solution 1 beats 100%: built-in function        
        # check all characters in the ransom note
        for c in set(ransomNote):
            # if we dont have enough characters from the magazine
            if ransomNote.count(c) > magazine.count(c):
                # we cant make it
                return False        
        # after all have been checked, we have enough from magazine for the ransom note
        return True
            
        # Solution 2 beats 85.26%: dictionary
        from collections import defaultdict          
        
        if not set(ransomNote).issubset(set(magazine)):
            return False
        n = defaultdict(int)   
        for c in magazine:
            n[c] += 1
        for c in ransomNote:
            n[c] -= 1
            if n[c] < 0:
                return False   
        return True
            
        