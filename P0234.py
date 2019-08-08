# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:14:10 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        l, p = 0, head
        while p:
            l += 1
            p = p.next
       
        pre, p = None, head 
        for _ in range(l//2):      
            pp, p.next = p.next, pre
            pre, p = p, pp                   
        
        if l % 2 == 1:
            p = p.next
        
        while p:
            if pre.val != p.val:
                return False
            pre, p = pre.next, p.next            
            
        return True