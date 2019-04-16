# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:11:20 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = root.val
        
        def helper(node):
            
            if not node:
                return float('-inf')
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)    
            
            sum_only_root = node.val
            sum_left_root = node.val + left_sum
            sum_right_root = node.val + right_sum           
            
            max_sum = max(sum_only_root, sum_left_root, sum_right_root)
            
            sum_all = node.val + left_sum + right_sum
            self.ans = max(self.ans, max_sum, sum_all)          
            
            return max_sum
           
        helper(root)
        
        return self.ans