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
        # d: the trie
        # l: levels of the trie
        # res: the max XOR
        d, l, res = {}, len(bin(max(nums)))-2, []
        # bs: the binary representation of each number, zero padded to length l
        bs = [map(int,bin(num)[2:].zfill(l)) for num in nums]
        # first build the Trie
        for num, b in zip(nums,bs):
            # start from the root
            node = d
            # build the Trie at each level
            for c in b:
                # add a new node if c has not appeared at this level before
                if c not in node:                
                    node[c] = {}              
                # otherwise move on to next level
                node = node[c]
            # at the end record this number at the bottom level
            node['val'] = num
        # then for each number, look for its complement, which gives the max XOR
        for num, b in zip(nums,bs):
            # start from the root
            node = d
            # check each digit
            for c in b:
                # choose complement of c if it exists
                # otherwise choose c itself
                node = node[1-c] if (1-c) in node else node[c] 
            # at the end update the max XOR
            res.append(node['val']^num)
        # return the max XOR
        return max(res)