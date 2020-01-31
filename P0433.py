# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:55:02 2020

@author: Tianqi Guo
"""

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if (not bank) or (end not in bank):
            return -1
        q, bank, res = [start], set(bank), 0
        while q:
            qq, res = [], res+1            
            for g in q:
                for i, c in enumerate(g):
                    for m in 'ACGT':
                        gg = g[:i]+m+g[i+1:]
                        if gg in bank:
                            if gg == end:
                                return res                        
                            qq.append(gg)
                            bank.remove(gg)
            q = qq
        return -1
                        
                        