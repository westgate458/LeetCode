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
        
        if not preorder:
            return None   
        
        root_indorder_idx = inorder.index(preorder[0])          
        
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:root_indorder_idx+1], inorder[:root_indorder_idx])
        root.right = self.buildTree(preorder[root_indorder_idx+1:], inorder[root_indorder_idx+1:])
        
        return root
            
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

test = Solution()
test.buildTree(preorder, inorder)