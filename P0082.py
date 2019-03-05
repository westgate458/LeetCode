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
        
        # dummy head node
        p = ListNode(float('nan'))
        # point dummy's next to head
        p.next = head
        # p0 points to the last node without duplicates
        p0 = p
        # p1 traverses the list
        p1 = head        
        
        # keep record of the previous value
        pre_num = float('nan')
        
        # if p1 has not reached the end of the list
        while p1:      
            # if current node is not equal to previous value nor the next value
            if (p1.val != pre_num) and (p1.next == None or p1.next.val != p1.val):               
                # add current node to the list without duplicates
                p0.next = p1
                p0 = p1
            # update the previous number
            pre_num = p1.val
            # traverse to next node
            p1 = p1.next
            
        # point the tail to None
        p0.next = None
        # return the list after duplicates are removed
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