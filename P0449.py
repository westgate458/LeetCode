# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:56:23 2020

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:  return ''
        q, s = deque([root]), [root.val]
        while q:
            n = q.popleft()
            if n.left:
                q.append(n.left)
                s += [n.left.val]
            else:
                s += [None]
            if n.right:
                q.append(n.right)
                s += [n.right.val]
            else:
                s += [None]
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        s = data
        root = TreeNode(s[0])
        q, p = deque([root]), 0
        while q:          
            node = q.popleft()
            p += 1
            if s[p] != None:
                node.left = TreeNode(s[p])                     
                q.append(node.left)
            p += 1
            if s[p] != None:
                node.right = TreeNode(s[p])
                q.append(node.right)            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))