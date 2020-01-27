# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:30:34 2020

@author: Tianqi Guo
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return None
        q, res = [root], []
        while q:
            vs, qq = [], []
            for n in q:
                vs.append(n.val)
                for c in n.children:
                    qq.append(c)
            res.append(vs)
            q = qq
        return res
            
            
        