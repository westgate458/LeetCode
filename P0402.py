# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:44:23 2020

@author: Tianqi Guo
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """        
        picked = [] 
        for n in num+'0':
            while picked and n < picked[-1] and k:
                picked.pop()
                k -= 1
            picked.append(n)        
        picked.pop()            
        while picked and picked[0] == '0':
            del picked[0]
        return ''.join(picked) if picked else '0'   