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
        # deal with trivial case
        if (not head) or (not head.next):            
            return head
        # counter of list length and traversal pointer
        c, p = 0, head
        # count number of nodes in the list
        while p:
            c += 1
            p = p.next            
        # sort the list by merging sorted halves
        return self.sortHalves(c, head)
    
    # subfunction sorting list segment of length c
    def sortHalves(self, c, head):
        # if only one node in current list
        if c == 1:
            # no need to sort, return itself
            return head
        # if there are more nodes in current list
        else:                
            # length counter and traversal pointer
            cc, p = 0, head           
            # count for the first half 
            while cc < c//2 - 1:
                p = p.next
                cc +=1
            # split current list into two halves
            left, right = head, p.next          
            # tail of the first half
            p.next = None                
            # sort the two halves first recursively
            pl = self.sortHalves(c//2, left)
            pr = self.sortHalves(c - c//2, right)
            # dummy head of the merged list and traversal pointer
            p = dummy = ListNode(0)
            # if both lists have not reached tail
            while pl and pr:
                # pick the smaller value between the two
                # to merge to the sorted list
                if pl.val < pr.val:
                    p.next = pl
                    pl = pl.next                        
                else:
                    p.next = pr
                    pr = pr.next   
                # update current node pointer in the sorted list                     
                p = p.next                
            # link the tail of merge list to whichever half with nodes left
            # since those nodes are always larger than the tail value
            p.next = pl or pr
        # return the sorted list after merging
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
                
                    
                
        