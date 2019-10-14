# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:19:53 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p_odd = p0_odd = ListNode(0)
        p_eve = p0_eve = ListNode(0)
        
        p, c = head, 0        
        while p:           
            c += 1
            if c % 2 == 1:
                p_odd.next, p_odd = p, p
            else:
                p_eve.next, p_eve = p, p                
            p = p.next

        p_odd.next, p_eve.next = p0_eve.next, None
        return p0_odd.next
                
                
            