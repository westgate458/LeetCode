# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:48:40 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # deal with trivial case
        if not root:
            return [] 
        # answer list           
        ans = []     
        # start traversal from root
        s = [root]            
        # continue traversal if still nodes to visit
        while s:
            # retrieve most recent node in stack
            node = s.pop()
            # place value of current node to answer list
            ans.append(node.val)            
            # first place left node into stack if exists
            if node.left:
                s.append(node.left)    
            # then place right node into stack if exists
            # for next round the right node is visited before left node
            if node.right:
                s.append(node.right)        
        
        # postorder traversal requires: left -> right -> root
        # current traversal order: root -> right -> left
        # return the reversed traversal result        
        return ans[::-1]