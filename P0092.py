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
        
        # dummy link head
        dm = ListNode(None)
        dm.next = head
        
        # traverse pointer
        p = head
        # position number count
        c = 0
        # previous node within segment
        pp = None
        # pointer to the node before target segment
        p0 = dm
  
        # continue traversing until tail
        while p:
            
            # update position counter
            c = c + 1
            # check if has reached the node before target segment
            if c == m - 1:
                # store current position
                p0 = p
                # move on to next node
                p = p.next                
            # check if within target segment
            elif m <= c <= n:
                # temporary pointer to current node
                pt = p
                # update traverse pointer to next node
                p = p.next
                # put previous node within segment after current node
                pt.next = pp
                # update previous node within segment to be current node
                pp = pt 
            # check if has past target segment
            elif c == n + 1:
                # put current node after the last node in target segment after reversing
                p0.next.next = p
                # put previous node within segment (now is the first node after reversing)
                # after the node before target segment
                p0.next = pp                
                # no need to continue, terminate traversing
                break  
            # if current node is of no interest
            else:
                # move on to next node
                p = p.next
        # if p is none, it means traverse has reached the end
        # so the tail is within the target segment
        if not p:
            # the last node in target segment after reversing should now be the tail
            p0.next.next = None
            # put previous node within segment (now is the first node after reversing)
            # after the node before target segment 
            p0.next = pp  
        
        # return reversed list
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