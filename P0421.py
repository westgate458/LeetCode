# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:47:37 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d, l, res = {}, len(bin(max(nums)))-2, []
        bs = [map(int,bin(num)[2:].zfill(l)) for num in nums]
        
        for num, b in zip(nums,bs):
            node = d
            for c in b:
                if c not in node:                
                    node[c] = {}              
                node = node[c]
            node['val'] = num

        for num, b in zip(nums,bs):
            node = d
            for c in b:
                node = node[1-c] if (1-c) in node else node[c] 
            res.append(node['val']^num)
        return max(res)