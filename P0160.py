# -*- coding: utf-8 -*-
"""
Created on Fri May 24 22:10:51 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Solution 1
        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1

        # Solution 2
        c1, c2 = 0, 0
        p1, p2 = headA, headB
        while p1:
            c1 += 1
            p1 = p1.next     
        while p2:
            c2 += 1
            p2 = p2.next        
        p1, p2 = headA, headB
        while c1 > c2:
            p1 = p1.next
            c1 -= 1        
        while c1 < c2:
            p2 = p2.next
            c2 -= 1 
        while p1 and p2:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next