# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:41:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
     
        def dfs(node, pre_sum):
            if node:
                current_sum = pre_sum*10 + node.val
                if not (node.left or node.right):
                    self.ans += current_sum
                else: 
                    dfs(node.left, current_sum)
                    dfs(node.right, current_sum)

        self.ans = 0
        if root:
            dfs(root, 0)
        return self.ans