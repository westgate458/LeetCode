# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:50:32 2018

@author: Tianqi Guo
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """ 
        
        p = head
        c = 0
        while p != None:
            c = c + 1
            if c == n + 1:
                pn = head
            else:
                if c > n + 1:
                    pn = pn.next            
            p = p.next
            
        if c <= n:
            return head.next
      
        pn.next = pn.next.next
        return head             

nums = [1,2,3,4,5]
n = 2
head = ListNode(nums[0])
p = head
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next
    
test = Solution()
p = test.removeNthFromEnd(head,n)
      
while p != None:
    print(p.val)      
    p = p.next