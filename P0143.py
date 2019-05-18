# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:46:25 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # deal with trivial case
        if not head:
            return None
        
        # start from begining
        p = head
        # list stores all nodes
        nodes = []
        
        # put all nodes into the list
        while p:
            nodes.append(p)
            p = p.next              
        
        # number of nodes
        l = len(nodes)
        # iterate over first half, link nodes back-and-forth
        ll = l//2        
        for i in range(ll):
            # link current node to the corresponding node in second half
            nodes[i].next = nodes[-i-1]
            # link that node in second half to next node
            nodes[-i-1].next = nodes[i+1]
        
        # link the last node in reordered list to None
        nodes[ll].next = None
        
        # return the reordered list
        return head