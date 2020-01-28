# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:42:25 2020

@author: Tianqi Guo
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        temp = Node(None, None, head, None)
        def DFS(node):
            p_child, p_next, tail = node.child, node.next, node
            if p_child:
                tail = DFS(p_child)    
                if node.next:
                    node.next.prev, tail.next = tail, node.next
                node.next, node.next.prev, node.child = node.child, node, None
            if p_next:
                tail = DFS(p_next)  
            return tail
        DFS(head)
        return temp.next