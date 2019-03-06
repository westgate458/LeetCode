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
        
        # dummy head for the nodes smaller than x
        p_l0 = ListNode(None)
        # dummy head for the nodes no less than x
        p_h0 = ListNode(None)        
        
        # pointer to the last nodes in each list
        p_l = p_l0
        p_h = p_h0
        
        # traverse pointer
        p = head  
        # continue traversing until tail of the list
        while p:
            
            # if current value smaller than x
            if p.val < x:
                # add current node to the 'smaller' list
                p_l.next = p
                p_l = p
            # if current value no less than x
            else:
                # add current node to the 'no less' list
                p_h.next = p
                p_h = p
            
            # go on to next node
            p = p.next
        
        # place the 'no less' list after the 'smaller' list
        p_l.next = p_h0.next
        # make tail node point to None
        p_h.next = None
        
        # return the partitioned list
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