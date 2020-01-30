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
        # deal with trivial case
        if not root:
            return None
        # q: the queue for BFS
        # res: the vals of all nodes
        q, res = [root], []
        # continue BFS when there are more levels
        while q:
            # vs: vals at current level
            # qq: nodes on the next level
            vs, qq = [], []
            # deal with each node at current level
            for n in q:
                # record its value
                vs.append(n.val)
                # add its children to next level to visit later
                for c in n.children:
                    qq.append(c)
            # add all values at current level to the result
            res.append(vs)
            # move on to next level
            q = qq
        # return all values
        return res
            
            
        