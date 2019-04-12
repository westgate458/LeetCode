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
        # deal with trivial case
        if not root:            
            return []
        # if current node is a leaf
        elif not root.left and not root.right:
            # if remaining sum is equal to current value
            if sum == root.val:                
                # current leaf is part of the desired path
                return [[root.val]]
            # if current leaf doesn't give the desired sum
            else:
                # return empty list
                return []
        # if current node is not a leaf
        else:     
            # 1) recursively check the child branches, which return lists of values that add up to the desired sum
            # 2) for the combined lists, add the value current node to each entry
            # 3) return the updated list of path values to previous level
            return [[root.val] + combo for combo in self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)]