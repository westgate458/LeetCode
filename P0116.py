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
        
        current_level = root
        next_level = root.left
        
        while current_level.left:
            
            current_level.left.next = current_level.right
            
            if current_level.next:
                current_level.right.next = current_level.next.left
                current_level = current_level.next
            else:
                current_level = next_level
                next_level = next_level.left
        
        return root  