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
        # deal with trivial case
        if not root:
            return None 
        # if we have found the node to delete
        if root.val == key:
            # if current node is a leaf
            if not root.left and not root.right:
                # simply return nothing so this node is deleted
                return None
            # if current node has a left child tree
            elif root.left:           
                # find the max value in the left sub tree
                node = root.left
                while node.right: node = node.right
                # now replace current value with the found max value
                # and delete the max value from the sub tree
                root.val, root.left = node.val, self.deleteNode(root.left, node.val)   
            # if current node has a right child tree
            else:             
                # find the min value in the right sub tree
                node = root.right
                while node.left: node = node.left
                # replace current value with the found min value
                # and delete the min value from the sub tree
                root.val, root.right = node.val, self.deleteNode(root.right, node.val)  
        # if we are still looking for the node to delete
        # locate the node in either of the subtrees, and update the subtree after deletion
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        # return the updated root after deletion
        return root