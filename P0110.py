# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:56:08 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """       
        
        # subfunction counts depth of current subtree and checks if balanced       
        def count_levels(root):
            
            # if current node is none
            if not root:
                # depth is 1
                return 1
            
            # count depth of left subtree
            left = count_levels(root.left)
            # if left tree not balanced
            if left == -1:
                # current BST is not balanced
                return -1
            
            # count depth of right subtree
            right = count_levels(root.right)
            # if right tree not balanced
            if right == -1:
                # current BST is not balanced
                return -1
            
            # if both subtrees are balanced
            # but their depths differ more than 1
            if abs(left-right) > 1:
                # current BST is not balanced
                return -1
            # if their depths differ less than 1
            else:
                # current BST is balanced, and return the depth
                return max(left, right) + 1
        
        # current BST is balanced if a depth is returned other than -1
        return count_levels(root) != -1