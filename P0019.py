# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:50:32 2018

@author: Tianqi Guo
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """ 
        
        # first pointer to visit each node
        p = head
        # second pointer to visit each node
        pn = None
        # count how many nodes in the list
        c = 0
        # visit each node until the tail
        while p != None:
            # set the first pointer to the next node
            p = p.next
            # update node number
            c = c + 1
            # if current node is n away from the head
            if c == n + 1:
                # start the second pointer from the head
                # so when p is pointing to the tail
                # pn is pointing to the node before the one to be removed
                pn = head
            else:
                # if current node is farther than n away from the head
                # i.e. the second pointer has already initialized
                if c > n + 1:
                    # set the second pointer to the next node
                    pn = pn.next  
        
        # if to remove the 1st node    
        if c <= n:
            # return the 2nd node
            return head.next
        # to remove the target node
        # set the 'next' pointer of the previous node 
        # to point to the node after target
        pn.next = pn.next.next
        # return head node
        return head             

nums = [1,2,3,4,5]
n = 2
head = ListNode(nums[0])
p = head
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next
    
test = Solution()
p = test.removeNthFromEnd(head,n)
      
while p != None:
    print(p.val)      
    p = p.next