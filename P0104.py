# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:30:25 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # deal with trivial case
        if not root:
            return 0      
        
        # Solution 1: recursion
        # max depth is the larger depth of subtrees plus 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1            
        
        # Solution 2, level order traversal
        # stack storing nodes at each level
        s = [root]
        # level counter
        c = 0
        # continue traversing while still nodes left
        while s:        
            # update level counter
            c = c + 1
            # continue to next level
            # update s and place children into s if not none    
            s = [child for n in s for child in [n.left, n.right] if child] 
        
        # return number of levels
        return c