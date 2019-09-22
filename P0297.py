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
        # deal with trivial case
        if not root:
            return ''
        # queue for BFS of the tree
        q = deque([root])
        # all values seen during the serialization
        s = [root.val]
        # continue BFS until all elements seen
        while q:
            # pop the next node
            n = q.popleft()
            # check its children
            # if it has a subtree, push it into queue, and record the value
            # if not, record None to mark the termination of path
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
        
        # somehow LeetCode does not enforce the return type
        # and return list is faster than string for deserialization
        #ss = ','.join(map(str, s))        
        #return ss
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # deal with trivial case
        if not data:
            return None
        # to deal with string input
        # s = [int(x) if x != 'None' else None for x in data.split(',')]
        # or just copy the input list
        s = data
        # construct tree from the root node
        root = TreeNode(s[0])
        # queue for constructed nodes
        q = deque([root])
        # pointer in s for next node
        p = 0
        # continue reconstruction all nodes are dealt with
        while q:          
            # next node to consider
            node = q.popleft()
            # p in s should point to its left child
            p += 1
            # if its left child exists
            if s[p] != None:
                # construct child node, and place it into the queue
                node.left = TreeNode(s[p])                     
                q.append(node.left)
            # same routine for right child
            p += 1
            if s[p] != None:
                node.right = TreeNode(s[p])
                q.append(node.right)       
        # return the reconstructed tree after deserialization
        return root        
       

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))