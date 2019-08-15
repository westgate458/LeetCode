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
        
        # first count how many nodes are there
        l, p = 0, head
        while p:
            l += 1
            p = p.next
       
        # reverse the first l/2 nodes
        # see P0206
        pre, p = None, head 
        for _ in range(l//2):      
            pp, p.next = p.next, pre
            pre, p = p, pp                   
        
        # in case of odd number of nodes, start comparison from next one
        if l % 2 == 1:
            p = p.next
        
        # start from the middle, compare nodes on left and right
        while p:
            # if not equal, original linked list is not Palindrome
            if pre.val != p.val:
                return False
            # move on to next ones
            pre, p = pre.next, p.next            
        
        # if all nodes are checked, original linked list is Palindrome
        return True