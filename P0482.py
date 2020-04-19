# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:15:10 2020

@author: Tianqi Guo
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # first remove all '-', and convert to upper case
        S = ''.join(S.split('-')).upper()
        # length of all characters
        l = len(S)        
        # see if we have remains after K-units
        b = l%K
        # steps:
        # 1) split the string by K-units
        # 2) join by '-'
        # 3) remove leading '-' if there is
        return('-'.join([S[:b]] + [S[idx:idx+K] for idx in xrange(b,l,K)]).lstrip('-'))    