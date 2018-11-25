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
        # create new node as the root
        root = ListNode(0)
        root.next = head
        
        # pointer to the previous node
        # before which all nodes are already dealt with
        prev = root        
        
        # pointer to traverse the node list
        p = head
        
        # waiting list of nodes to be reversed
        ps = []
        
        # count how many nodes are in the waiting list
        c = 0
        
        # stop traverse at the end of the list
        while p:
            
            # update counter and add current node to 'to-be-reversed' list
            c = c + 1 
            ps.append(p)
            p = p.next
            
             # if k nodes are in the waiting list
            if c == k:
                
                # take lastly dealt node as previous node
                pt = prev
                # if the waiting list is not empty yet
                while ps:
                    # let previous node point to the current last one in waiting list      
                    pt.next = ps.pop(-1)
                    # update previous node as current node
                    pt = pt.next        
                # make the lastly dealt node as previous node    
                prev = pt
                # the lastly dealt node should point to None for now
                prev.next = None
                # no element currently in the waiting list
                c = 0
        
        # deal with the special situation 
        # if the waiting list has fewer than k elements in the end
        pt = prev
        # add all elements in the waiting list to new node list without reversing
        while ps:
            pt.next = ps.pop(0)
            pt = pt.next      
        
        # return the reversed list of nodes
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

