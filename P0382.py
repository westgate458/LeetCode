# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:53:54 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1 beats 97.28%: cheats
from random import choice
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return choice(self.nums)

## Solution 2 beats 45.92%: Reservoir Sampling
#from random import randint
#class Solution(object):
#
#    def __init__(self, head):
#        """
#        @param head The linked list's head.
#        Note that the head is guaranteed to be not null, so it contains at least one node.
#        :type head: ListNode
#        """
#        self.head = head
#        
#    def getRandom(self):
#        """
#        Returns a random node's value.
#        :rtype: int
#        """
#        counter, val, p = 0, self.head.val, self.head.next                
#        while p:
#            counter += 1         
#            if randint(0, counter) == 0: val = p.val
#            p = p.next        
#        return val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()