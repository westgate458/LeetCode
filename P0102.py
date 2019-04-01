# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:06:32 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # deal with trivial case
        if not root:            
            return []        
        
        # stack storing nodes at each level
        s = [root]
        # answer list storing values from each level
        ans = []
        
        # continue traversing while still nodes left
        while s:         
            
            # append values from current level to answer list
            ans.append([n.val for n in s])   
            # continue to next level
            # update s and place children into s if not none
            s = [child for n in s for child in [n.left, n.right] if child]              
        
        # return the values at each level
        return ans