# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:33:45 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p, pre = head, dummy        
        while p:
            if p.val != val:
                pre.next = p
                pre = p
            p = p.next
        pre.next = p            
        return dummy.next