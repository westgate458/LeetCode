# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:03:37 2019

@author: Tianqi Guo
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        p_l0 = ListNode(None)
        p_h0 = ListNode(None)        
        
        p_l = p_l0
        p_h = p_h0
        
        p = head  
        while p:
            
            if p.val < x:
                p_l.next = p
                p_l = p
            else:
                p_h.next = p
                p_h = p
            p = p.next
        
        p_l.next = p_h0.next
        p_h.next = None
        
        return p_l0.next
                
         
nums = [1,4,3,2,5,2]
x = 3
head = ListNode(nums[0])
p = head
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next
    
test = Solution()
p = test.partition(head,x)

while p:
    print(p.val)      
    p = p.next