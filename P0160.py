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
        # Solution 1: two points only, cross-restart
        # two pointers to traverse linked nodes
        p1, p2 = headA, headB
        # continue traversal until two pointers meet
        while p1 != p2:
            # if first linked nodes have not reached the tail
            if p1:
                # move on to next node
                p1 = p1.next
            # if first linked nodes have reached the tail
            else:
                # restart traversal from the head of 2nd linked nodes
                p1 = headB
            
            # if second linked nodes have not reached the tail
            if p2:
                # move on to next node
                p2 = p2.next
            # if second linked nodes have reached the tail
            else:
                # restart traversal from the head of 1st linked nodes
                p2 = headA
        
        # the cross-restart eliminates the length difference of the two
        # the two pointers will meet either at the intersectional node
        # or at the tails (both are None) of the two if no intersection exists
        return p1

        # Solution 2: count number of nodes
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