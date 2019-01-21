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
        if not head:
            return []
        
        c = 1
        p = head
        while p.next:
            c = c + 1
            p = p.next
        tail = p

        k = k%c

        p = head
        while c > k + 1:
            c = c - 1
            p = p.next

        tail.next = head
        head = p.next
        p.next = None
        
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