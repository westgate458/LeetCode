# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:40:36 2018

@author: Tianqi Guo
"""

 # Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        head = ListNode(float('-inf'))
        p = head
        
        while (p1 != None) or (p2 != None):
             if (p1 == None):
                p.next = p2                
                p2 = None
                continue
             if (p2 == None):
                p.next = p1                
                p1 = None
                continue
             if (p1.val <= p2.val):
                p.next = ListNode(p1.val)
                p = p.next
                p1 = p1.next
                continue
             if (p2.val <= p1.val):
                p.next = ListNode(p2.val)
                p = p.next
                p2 = p2.next
                continue                    
        return head.next  
        
nums = [1,2,4]
l1 = ListNode(nums[0])
p = l1
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next    

nums = [1,3,4]    
l2 = ListNode(nums[0])
p = l2
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next
    
test = Solution()
p = test.mergeTwoLists(l1,l2)
      
while p != None:
    print(p.val)      
    p = p.next