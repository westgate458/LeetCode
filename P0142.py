# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:05:08 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.visited = set()
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head in self.visited:            
            return head
        else:
            self.visited |= set([head])            
            return self.detectCycle(head.next)