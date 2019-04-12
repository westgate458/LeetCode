# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:53:11 2019

@author: Tianqi Guo
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """     
        
        # deal with trivial case
        if not root:            
            return
        
        # pointer for current level traversal
        current_level = root
        # pointer for next level
        next_level = root.left
        
        # continue connecting until leaf level
        # nodes on current level are already connected
        # now connect all child nodes on next level
        while current_level.left:
            
            # connect left child node to right child node
            current_level.left.next = current_level.right
            
            # if there are more nodes on current level to the right
            if current_level.next:
                # connect right child node of current node to 
                # the left child node of the next node on current level
                current_level.right.next = current_level.next.left
                # move on to the next node on current level
                current_level = current_level.next
            # if has reached the last node on current level
            else:
                # move on to next level
                current_level = next_level
                # update next level pointer to the first left child node
                next_level = next_level.left
        
        # return connected tree
        return root  
    
    
    
    