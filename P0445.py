# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:42:24 2020

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, p = 0, l1
        while p: n1, p = n1*10+p.val, p.next
        n2, p = 0, l2
        while p: n2, p = n2*10+p.val, p.next
        p = t = ListNode(None)
        for c in str(n1+n2):
            p.next = ListNode(c)
            p = p.next
        return t.next 
        
        
        
        