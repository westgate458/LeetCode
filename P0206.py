# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:49:44 2019

@author: Tianqi Guo
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1 beats 97.21%: recursive
        def DFS(n):   
            tail = DFS(n.next) if n.next.next else n.next
            n.next.next = n
            return tail
        if not head or not head.next:
            return head
        res, head.next = DFS(head), None
        return res
        
        # Solution 2 beats 88.78%: iterative
        # pre: previous node
        # p: current node
        pre, p = None, head 
        # continue traversal until the tail
        while p:            
            # copy next node to temporary pointer pp
            # place previous node after current node
            pp, p.next = p.next, pre
            # current node is now previous node
            # continue traversal to next node
            pre, p = p, pp  
        # after reaching tail
        # the pre pointer is now the new head
        return pre
