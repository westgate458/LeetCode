# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:03:09 2019

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
        
        p = ListNode(float('nan'))
        p.next = head
        p0 = p
        p1 = head        
        
        pre_num = float('nan')
        
        while p1:      

            if (p1.val != pre_num) and (p1.next == None or p1.next.val != p1.val):               
                p0.next = p1
                p0 = p1
            
            pre_num = p1.val
            p1 = p1.next
        
        p0.next = None
        return p.next
            

        
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