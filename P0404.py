# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:53:54 2020

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # deal with trivial case
        if not root:
            return 0
        # start from the root
        s = [(root,False)]
        # the sum
        res = 0
        # start the DFS
        while s:
            # current node
            n, isLeft = s.pop()
            # check if current node is a leaf
            if not n.left and not n.right:
                # check if it is a left leaf
                if isLeft:
                    # update the sum
                    res += n.val
            # if current node has a left child
            if n.left:
                # place it in the stack to visit later
                s.append((n.left,True))
            # same operation for the right child
            if n.right:
                s.append((n.right,False))
        # the sum of all left leaves
        return res