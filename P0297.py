# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:39:04 2019

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
        if not root:
            return ''
        
        q = deque([root])
        s = [root.val]
        
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
        #ss = ','.join(map(str, s))        
        #return ss
        return s


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        #s = [int(x) if x != 'None' else None for x in data.split(',')]
        s = data
        
        root = TreeNode(s[0])
        level = deque([root])
        p = 0
        while level:
            new_level = deque([])
            while level:
                node = level.popleft()
                p += 1
                if s[p] != None:
                    node.left = TreeNode(s[p])                     
                    new_level.append(node.left)
                p += 1
                if s[p] != None:
                    node.right = TreeNode(s[p])
                    new_level.append(node.right)
            level = new_level
        return root        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))