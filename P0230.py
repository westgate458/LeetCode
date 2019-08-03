# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:51:01 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        # Solution 1: iteratively     
        # In-order traversal will result in sorted numbers from small to large
        # start traversal from root, counting c till k
        s, node, c = [], root, 0 
        # traversal goes on forever since it is guaranteed the answer exists
        while True:            
            # if current node is not None            
            while node:
                # place it into the stack
                s.append(node)
                # move on to its left child
                node = node.left            
            # when the while loop ends, it means the left child is None
            # and the parent of that child is the smallest in its own subtree
            # pop this parent
            node = s.pop()
            # now this node is visited, and it is the c-th smallest number
            c += 1            
            # if we have counted to k
            if c == k:
                # value of this node is the k-th smallest number
                return node.val            
            # if we have not reached k
            # move on to its right child
            node = node.right        
        
        # Solution 2: recursively    
        def helper(root, k):            
            if not root:
                return (0, None)
            nodes_left, res = helper(root.left, k)   
            if res != None:
                return (None, res)
            elif k == nodes_left + 1:
                return (None, root.val)
            else:
                nodes_right, res = helper(root.right, k - (nodes_left + 1))
                if res:
                    return (None, res)
                else:
                    return (nodes_left + nodes_right + 1, None)                
        _, res = helper(root, k)  
        return res
                