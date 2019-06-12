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
        self.s = []
        self.p = root  
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """        
        while (self.p) or (self.s):
            if (self.p):
                self.s.append(self.p)
                self.p = self.p.left
            else:
                self.p = self.s.pop()
                num = self.p.val
                self.p = self.p.right
                return num 

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """        
        return (self.p) or (self.s)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()