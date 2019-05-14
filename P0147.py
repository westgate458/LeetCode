# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:37:32 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        # Solution 1
        pre = dummy = ListNode(-float('inf'))          
        cur = dummy.next = head  
        
        while cur and cur.next:
            
            next_val = cur.next.val
            if cur.val < next_val:
                cur = cur.next
            else:
                if pre.next.val > next_val:
                    pre = dummy
                while next_val > pre.next.val:
                    pre = pre.next
                
                node = cur.next
                cur.next = node.next
                node.next = pre.next
                pre.next = node                
        
        return dummy.next
        
        # Solution 2
        if (not head) or (not head.next):
            return head
        
        p = dummy = ListNode(-float('inf'))            
        dummy.next = head
             
        unsorted_head = head.next
        head.next = None
        
        while unsorted_head:
            current = unsorted_head
            unsorted_head = unsorted_head.next
            current.next = None
            
            if p.next.val > current.val:
                p = dummy
            while p.next and (p.next.val < current.val):
                p = p.next     

            current.next = p.next
            p.next = current
        
        return dummy.next
        
            
        