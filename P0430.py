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
        # deal with trivial case
        if not head:
            return None
        # subfunction for dealing with each node
        def DFS(node):
            # temporary pointer the next node
            # tail is temporarily set to itself
            p_next, tail = node.next, node
            # if current node has a child
            if node.child:
                # first we DFS its child and find the tail
                tail = DFS(node.child)    
                # if current node has a next node
                if node.next:
                    # we append the next node to the tail from its child
                    node.next.prev, tail.next = tail, node.next
                # flatten by append the child link as the next one
                node.next, node.next.prev, node.child = node.child, node, None
            # if previously current node has a next one
            if p_next:
                # now we DFS the next node and get the real tail
                tail = DFS(p_next)  
            # return the actual tail so we can deal with previous nodes
            return tail
        # start DFS from the head
        DFS(head)
        # return the flattened linked nodes
        return head