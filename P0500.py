# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:06:15 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set(['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'])
        s2 = set(['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'])
        s3 = set(['z','x','c','v','b','n','m','Z','X','C','V','B','N','M'])             
        return [word for word in words if (set(word).issubset(s1) or set(word).issubset(s2) or set(word).issubset(s3))]