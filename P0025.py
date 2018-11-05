# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 21:56:34 2018

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        root = ListNode(0)
        root.next = head
        prev = root        
        p = head
        ps = []
        c = 0
        while p:
            c = c + 1 
            ps.append(p)
            p = p.next
            if c % k == 0:
                pt = prev
                while ps:
                    pt.next = ps.pop(-1)
                    pt = pt.next          
                prev = pt
                prev.next = None
        pt = prev
        while ps:
            pt.next = ps.pop(0)
            pt = pt.next            
        return root.next        

nums = [1,2,3,4,5]   
k = 3     
l1 = ListNode(nums[0])
p = l1
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next  
    
test = Solution()
p = test.reverseKGroup(l1,k)
while p != None:
    print(p.val)      
    p = p.next

