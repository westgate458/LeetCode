# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:23:08 2019

@author: Tianqi Guo
"""

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        elif not root.left and not root.right:
            if sum == root.val:                
                return [[root.val]]
            else:
                return []
        else:     
            return [[root.val] + combo for combo in self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)]