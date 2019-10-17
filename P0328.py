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
        
        # pointers to the heads of odd and even lists
        p_odd = p0_odd = ListNode(0)
        p_eve = p0_eve = ListNode(0)
        
        # traverse pointer and counter
        p, c = head, 0        
        # continue traverse until tail
        while p:           
            # update counter
            c += 1
            # depending on it is odd or even
            # append this node to corresponding lists
            if c % 2 == 1:
                p_odd.next, p_odd = p, p
            else:
                p_eve.next, p_eve = p, p             
            # move on to next
            p = p.next
        # now place the even list at the tail of the odd list
        p_odd.next, p_eve.next = p0_eve.next, None
        # return the merged list
        return p0_odd.next
                
                
            