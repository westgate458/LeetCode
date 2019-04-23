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
        
        # the dfs for traversal
        def dfs(node, pre_sum):
            # if current node is not None
            if node:
                # sum from root up to current level
                current_sum = pre_sum*10 + node.val
                # if current node is a leaf
                if not (node.left or node.right):
                    # add current sum to the answer
                    self.ans += current_sum
                # if current node has subtrees
                else: 
                    # calculate the sums for subtrees
                    dfs(node.left, current_sum)
                    dfs(node.right, current_sum)
        
        # the total sum
        self.ans = 0
        # if root is not trivial
        if root:
            # start dfs from root
            dfs(root, 0)
        # return total sum
        return self.ans