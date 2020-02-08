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
        # deal with trivial cases
        if (not bank) or (end not in bank):
            return -1
        # q: queue for BFS
        # bank: convert to set for hash
        # res: number of mutations needed
        q, bank, res = [start], set(bank), 0
        # continue BFS until target has reached
        while q:
            # temporal new queue, and update mutation count
            qq, res = [], res+1            
            # check each gene in current generation of genes
            for g in q:
                # try to mutate each char
                for i, c in enumerate(g):
                    # try all possible mutations
                    for m in 'ACGT':
                        # form new gene
                        gg = g[:i]+m+g[i+1:]
                        # see if new gene is in the bank
                        if gg in bank:
                            # if new gene is the target
                            if gg == end:
                                # return number of mutations so far
                                return res         
                            # place current new gene in next generation of queue
                            qq.append(gg)
                            # remove this gene from bank so we won't turn back in circles
                            bank.remove(gg)
            # move on to next generation
            q = qq
        # if we didn't find the target, it is not reachable
        return -1
                        
                        