# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:54:42 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # deal with trivial case
        if not preorder:
            return None   
        
        # find the position of the node value in the inorder traversal
        # this is also the number of elements in left subtree
        # values before it -> left subtree
        # values after it -> right subtree
        root_indorder_idx = inorder.index(preorder[0])          
        
        # construct root node
        root = TreeNode(preorder[0])
        # construc left subtree recursively
        root.left = self.buildTree(preorder[1:root_indorder_idx+1], inorder[:root_indorder_idx])
        # construc right subtree recursively
        root.right = self.buildTree(preorder[root_indorder_idx+1:], inorder[root_indorder_idx+1:])
        
        # return root node with its subtrees
        return root
            
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

test = Solution()
test.buildTree(preorder, inorder)