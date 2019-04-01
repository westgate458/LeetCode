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
        
        # deal with trivial case
        if not inorder:
            return None   
        
        # pop the last element from post order traversal -> the root value
        root_val = postorder.pop()
        # find the position of the node value in the inorder traversal
        # this is also the number of elements in left subtree
        # values before it -> left subtree
        # values after it -> right subtree
        root_indorder_idx = inorder.index(root_val)          
        
        # construct root node
        root = TreeNode(root_val)
        # construct the right subtree first
        # afterwards all remaining elements in postorder belong to left subtree
        root.right = self.buildTree(inorder[root_indorder_idx+1:], postorder)
        # construct the left subtree with remaining elements
        root.left = self.buildTree(inorder[:root_indorder_idx], postorder)        
        
        # return root node with its subtrees
        return root
    
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

test = Solution()
test.buildTree(inorder, postorder)