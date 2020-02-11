# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:55:33 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Solution 1 beats 97.02%: direct delete
        # 1) copy next value to current value
        # 2) delete next node
        node.val, node.next = node.next.val, node.next.next
        
        # Solution 2 beats 32.54%: shift values
        while node.next.next:
            node.val, node = node.next.val, node.next
        node.val, node.next = node.next.val, None