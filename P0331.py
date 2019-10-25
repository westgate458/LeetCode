# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:55:04 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """        
        # Solution 1 beats 99.43%: counting slots
        # s: current available slots for nulls, must be and only be 0 after whole tree is traversed
        s = 1
        # steps:
        # 1) preorder.split(','): split original string by ','
        # 2) map(lambda c: c == '#', _): check if each node is null
        # 3) traverse the whole tree
        for is_null in map(lambda c: c == '#', preorder.split(',')):
            # if before whole tree is traversed, the slot is 0
            # then the tree is not valid
            if not s: return False     
            # if current node is not null, then we have one more slot
            # if current node is null, we have one fewer slot
            s = s - 1 if is_null else s + 1              
        # after whole tree is traversed, a valid tree should have 0 slot for nulls
        return not s
        
#        # Solution 2 beats 94.59%: using stack
#        nodes = preorder.split(',')
#        l = len(nodes)
#        if nodes[0] == '#':
#            return l == 1  
#        s = [[nodes[0],0]]
#        p = 0        
#        for p in xrange(1,l):
#            if nodes[p] == '#':
#                if not s:
#                    return False
#                s[-1][1] += 1
#                while s and s[-1][1] == 2:
#                    s.pop()                    
#                    if s:
#                        s[-1][1] += 1
#                    elif p < l - 1:
#                        return False
#            else:
#                s.append([nodes[0],0])
#        return not s