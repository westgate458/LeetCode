# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:35:52 2018

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
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
        
        # waiting list of nodes to be swapped
        ps = []
        
        # count how many nodes are visited
        c = 0
        
        # stop traverse at the end of the list
        while p:
            
            # update counter and add current node to 'to-be-swapped' list
            c = c + 1 
            ps.append(p)
            p = p.next
            
            # if two nodes are in the waiting list
            if c % 2 == 0:
                
                # take lastly dealt node as previous node
                pt = prev                
                # if the waiting list is not empty yet
                while ps:
                    # let previous node point to the last one in waiting list                    
                    pt.next = ps.pop(-1)
                    # update previous node as current node
                    pt = pt.next          
                # make the lastly dealt node as previous node
                prev = pt
                # the lastly dealt node should point to None for now
                prev.next = None
        
        # deal with the special situation 
        # if the waiting list has fewer than 2 elements in the end
        pt = prev
        # add all elements in the waiting list to new node list without swapping
        while ps:
            pt.next = ps.pop(0)
            pt = pt.next            
        
        # return the swapped list of nodes
        return root.next        

nums = [1,2,3,4,5]        
l1 = ListNode(nums[0])
p = l1
for i in range(1,len(nums)):
    p.next = ListNode(nums[i])
    p = p.next  
    
test = Solution()
p = test.swapPairs(l1)
while p != None:
    print(p.val)      
    p = p.next