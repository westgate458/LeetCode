# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:49:44 2019

@author: Tianqi Guo
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre, p = None, head 
        while p:            
            pp, p.next = p.next, pre
            pre, p = p, pp  
        return pre
