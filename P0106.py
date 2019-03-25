# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:52:33 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        if not inorder:
            return None   
 
        root_val = postorder.pop()
        root_indorder_idx = inorder.index(root_val)          
        
        root = TreeNode(root_val)
        root.right = self.buildTree(inorder[root_indorder_idx+1:], postorder)
        root.left = self.buildTree(inorder[:root_indorder_idx], postorder)        
        
        return root
    
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

test = Solution()
test.buildTree(inorder, postorder)