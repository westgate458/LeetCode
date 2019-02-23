# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:03:58 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
                
        p = head        
               
        while p:      
            
            pt = p.next
            
            while (pt != None) and (pt.val == p.val):        
                pt = pt.next      
                
            p.next = pt
            p = pt
                   
        return head
            

        
nums = [1,1,1,2,3]
n = 2
head = ListNode(nums[0])
p = head
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next

test = Solution()
    
p = test.deleteDuplicates(head)
while p != None:
    print(p.val)      
    p = p.next