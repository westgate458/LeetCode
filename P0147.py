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
        
        # Solution 1: only alter position if current node is out-of-place
        # pointer to previous node, start from dummy
        pre = dummy = ListNode(-float('inf'))          
        # pointer to current node, start from head
        cur = dummy.next = head  
        
        # if have not reached the tail
        while cur and cur.next:
            # get the value of next node
            next_val = cur.next.val
            # if current node is no larger than the next one
            if cur.val <= next_val:
                # move on to next node
                cur = cur.next
            # if current node is larger than the next one
            # i.e. the next node need to be moved forward
            else:
                # if next value is larger than the previous node
                if pre.next.val > next_val:
                    # it need to be placed before previous node
                    # start searching from dummy
                    pre = dummy
                # start from previous node
                # search for the first node larger than next value
                while next_val > pre.next.val:
                    pre = pre.next                
                # temporary pointer pointing to next node
                node = cur.next
                # remove next node from the list
                cur.next = node.next
                # insert next node after previous node
                node.next = pre.next
                # previous node now links to the next node
                pre.next = node 
        # return the sorted list
        return dummy.next
        
        # Solution 2: merge sorted and unsorted parts of the list
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
        
            
        