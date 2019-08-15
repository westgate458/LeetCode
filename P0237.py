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
        
        # 1) copy next value to current value
        # 2) delete next node
        node.val, node.next = node.next.val, node.next.next