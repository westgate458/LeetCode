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
        
        if not head:
            return None
        
        p = head
        nodes = []
        
        while p:
            nodes.append(p)
            p = p.next              
        
        l = len(nodes)
        ll = l//2
        for i in range(ll):
            nodes[i].next = nodes[-i-1]
            nodes[-i-1].next = nodes[i+1]
        
        nodes[ll].next = None
        
        return head