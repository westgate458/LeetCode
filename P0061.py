# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:41:46 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # deal with trivial case
        if not head:
            return []
        
        # count number of nodes
        c = 1
        p = head
        # continue counting till tail of the list
        while p.next:
            c = c + 1
            p = p.next
        tail = p
        
        # avoid redundant rotations
        k = k%c
        
        # find the last k nodes
        p = head
        # stop when current node is the new tail
        while c > k + 1:
            c = c - 1
            p = p.next
        
        # place current head after the tail
        tail.next = head
        # update head pointer
        head = p.next
        # place current node at the tail
        p.next = None
        
        # return the new head
        return head
         
k = 4
nums = [0,1,2]  
l1 = ListNode(nums[0])
p = l1
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next      

test = Solution()
p = test.rotateRight(l1,k)
while p:
    print(p.val)      
    p = p.next