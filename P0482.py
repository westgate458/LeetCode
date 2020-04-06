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
        
        S = ''.join(S.split('-')).upper()
        l = len(S)
        a, b = divmod(l,K)        
        res = [S[:b]]
        for idx in xrange(b,l,K): res.append(S[idx:idx+K])
        return('-'.join(res).lstrip('-'))