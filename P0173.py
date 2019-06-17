# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:26:47 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # stack for iterative pre-order tree traversal
        self.s = []
        # start traversal from root
        self.p = root  
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """        
        # continue traversal until all nodes are visited
        while (self.p) or (self.s):
            # if current node is not None
            if (self.p):
                # place current node into stack
                self.s.append(self.p)
                # move on to its left child
                self.p = self.p.left
            # if current node is None
            else:
                # look at to previous node in the stack
                self.p = self.s.pop()
                # this node is the next small number
                num = self.p.val
                # move on to its right child
                self.p = self.p.right
                # return the next small number
                # and pause traversal
                return num 

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """        
        # if there is a next small number
        # the traversal must be able to continue
        return (self.p) or (self.s)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()