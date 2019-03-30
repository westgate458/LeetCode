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
        
                
        def count_levels(root):
            
            if not root:
                return 1
            
            left = count_levels(root.left)
            if left == -1:
                return -1
            
            right = count_levels(root.right)
            if right == -1:
                return -1
                
            if abs(left-right) > 1:
                return -1
            else:
                return max(left, right) + 1
        
        return count_levels(root) != -1