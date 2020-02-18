# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:56:01 2020

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """        
        if not root:
            return None        
        if root.val == key:    
            if not root.left and not root.right:
                return None
            elif root.left:                  
                node = root.left
                while node.right: node = node.right
                root.val, root.left = node.val, self.deleteNode(root.left, node.val)        
            else:                
                node = root.right
                while node.left: node = node.left
                root.val, root.right = node.val, self.deleteNode(root.right, node.val)    
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root