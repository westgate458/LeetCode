# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:21:46 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # deal with trivial case
        if not root:            
            return 0
        
        # level order traversal
        # queue for nodes to be visited
        s = [root]
        # level counter
        l = [1]    
       
        while s:
            # pop the first node in queue, and its level number
            n = s.pop(0)
            c = l.pop(0)
            # if left branch exists
            if n.left:
                # place left child and its level numner into queue
                s.append(n.left)
                l.append(c+1)
            # same handling with right branch
            if n.right:
                s.append(n.right)     
                l.append(c+1)
            # if current node is a leaf
            if not n.left and not n.right:
                # return the level of current node
                # which is the min depth
                return c                    
    
        return