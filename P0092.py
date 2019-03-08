# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:15:42 2019

@author: Tianqi Guo
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        dm = ListNode(None)
        dm.next = head
        
        p = head
        c = 0
        pp = None
        p0 = dm
  
        while p:
            
            c = c + 1            
            
            if c == m - 1:
                p0 = p
                p = p.next                
            
            elif m <= c <= n:
                pt = p
                p = p.next
                pt.next = pp
                pp = pt 
                
            elif c == n + 1:
                p0.next.next = p
                p0.next = pp                
                break  
            
            else:
                p = p.next
        
        if not p:
            p0.next.next = None
            p0.next = pp  
            
        return dm.next
        
nums = [1, 2, 3, 4, 5]
m = 2
n = 5

head = ListNode(nums[0])
p = head
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next

test = Solution()
p = test.reverseBetween(head, m, n)

while p:
    print(p.val)      
    p = p.next