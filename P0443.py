# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:08:11 2020

@author: Tianqi Guo
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p0 = pp = pt = lc = len(chars)-1
        while pp>=0:
            nn = []
            while pp >= 0 and chars[pp] == chars[p0]:
                pp -= 1
            if p0 - pp > 1:
                nn = list(str(p0-pp))
            ln = len(nn)
            chars[pt-ln:pt+1] = [chars[p0]]+nn                        
            p0, pt= pp, pt-ln-1
        l = lc - pt
        chars[:l] = chars[-l:]    
        return(l)