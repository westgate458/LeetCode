# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:38:52 2019

@author: Tianqi Guo
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        # hash table dictionary[original node]: cloned node
        self.visited = {}  
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        # if trivial case or reached end
        if not head:
            return None                
        
        # create a new node            
        new_head = Node(head.val, None, None)  
        # record original node and cloned node in the hash table
        self.visited[head] = new_head        
        
        # continue to next node
        new_head.next = self.copyRandomList(head.next)
        # when return from recursion, all nodes have been created and recorded in the hash table
        
        # if original node has a random pointer
        if head.random:
            # assign random pointer of the cloned node
            new_head.random = self.visited[head.random]        
        
        # return the cloned node
        return new_head
        
head = Node(-1, None, None)
test = Solution()
print test.copyRandomList(head).val