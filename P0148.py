# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:38:18 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): 
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):            
            return head
        c, p = 0, head
        while p:
            c += 1
            p = p.next            
        return self.sortHalves(c, head)
    
    def sortHalves(self, c, head):
        
        if c == 1:
            return head
        else:                
            cc, p = 0, head           
            while cc < c//2 - 1:
                p = p.next
                cc +=1
            left, right = head, p.next            
            p.next = None
                
            p = dummy = ListNode(0)
            pl = self.sortHalves(c//2, left)
            pr = self.sortHalves(c - c//2, right)
                
            while pl and pr:
                if pl.val < pr.val:
                    p.next = pl
                    pl = pl.next                        
                else:
                    p.next = pr
                    pr = pr.next                        
                p = p.next                
            p.next = pl or pr

        return dummy.next
            
nums = [-1,5,3,4,0]                
dummy = ListNode(0)
p = dummy
for num in nums:
    p.next = ListNode(num)
    p = p.next

head = dummy.next
p = head
while p:
    print p.val
    p = p.next                        
                
test = Solution()
p = test.sortList(head)
while p:
    print p.val
    p = p.next 
                
                
                
                
                
                
                
                
                    
                
        