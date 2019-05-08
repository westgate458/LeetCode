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


# Solution 1
class Solution(object):    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        p1 = p2 = head        
        while p2 and p2.next:            
            p1 = p1.next
            p2 = p2.next.next            
            if p1 == p2:                
                p1 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1        
        return None

# Solution 2
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