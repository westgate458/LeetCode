# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:05:08 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1: use constant space
class Solution(object):    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """    
        # initialize two pointers
        p1 = p2 = head        
        # continue traverse until tails
        while p2 and p2.next:          
            # speed of second pointer is double the speed of first pointer
            p1 = p1.next
            p2 = p2.next.next            
            # if two pointers meet (at A)
            # the second pointer has traveled one more cycle than first pointer
            if p1 == p2:                
                # restart the first pointer from the head
                p1 = head
                # continue traverse until two pointers meet again (at B)
                while p1 != p2:
                    # move on to next nodes
                    p1 = p1.next
                    p2 = p2.next
                # the node where two pointers meet is where the cycle starts
                # 2 * (head->A) == head->A + cycle (A->A)
                # head->A == A->A
                # head->B->A == A->B->A
                # head->B == A-B
                return p1        
        # if tails are found there is no cycle
        return None

# Solution 2: use extra space
#class Solution(object):
#    def __init__(self):
#        self.visited = set()
#        
#    def detectCycle(self, head):
#        """
#        :type head: ListNode
#        :rtype: ListNode
#        """
#        if not head:
#            return None
#        if head in self.visited:            
#            return head
#        else:
#            self.visited |= set([head])            
#            return self.detectCycle(head.next)