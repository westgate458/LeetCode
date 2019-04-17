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
        
        def dfs(node):        
            
            sums = [0]
            if node.left:
                sums += [dfs(node.left)]
            if node.right:
                sums += [dfs(node.right)]                               
            
            sum_linked_out = max(sums) + node.val            
            sum_with_in = sum(sums) + node.val
            
            self.ans = max(self.ans, sum_linked_out, sum_with_in)          
            
            return sum_linked_out
        
        self.ans = root.val
        dfs(root)
        
        return self.ans