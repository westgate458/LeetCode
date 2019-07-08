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
        # dummy node to point to the new head
        dummy = ListNode(0)
        # p: start traversal from head
        # pre: last element of already examined list
        p, pre = head, dummy        
        # continue traversal until the tail
        while p:
            # if current value is not to be removed
            if p.val != val:
                # update the pre pointer
                # add current node to result list
                pre.next = p
                pre = p
            # move on to next node
            p = p.next
        # add last element (might be None) to result list
        pre.next = p            
        # return the new head
        return dummy.next