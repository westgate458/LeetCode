# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:06:19 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # deal with trivial case
        if not root:
            return True
        
        # start BFS from the root
        l = [root]
        # bounds for each node to comply
        bounds = [(-float('Inf'),float('Inf'))]
        
        # continue until all nodes are checked
        while l:
            
            # take the earliest node put in the queue
            # and its value bounds
            node = l.pop(0)
            low, high = bounds.pop(0)
            
            # if left child is not empty
            if node.left:
                # its value need to be larger than the lower bound of its parent
                # and smaller than its parent
                if low < node.left.val < node.val:
                    # if it's bounded then put it in queue to check its children
                    l.append(node.left)
                    # also put its bounds in queue
                    bounds.append((low, node.val))
                # if it's not bounded
                else:
                    # this node is not valid, and the BST is not valid
                    return False
                
            # same procedure for right child
            if node.right:
                if node.val < node.right.val < high:
                    l.append(node.right)
                    bounds.append((node.val, high))
                else:
                    return False 
        
        # if all nodes checked and validated
        # current BST is valid
        return True