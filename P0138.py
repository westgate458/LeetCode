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
        self.visited = {}  
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None                
            
        new_head = Node(head.val, None, None)  
        
        self.visited[head] = new_head        
        new_head.next = self.copyRandomList(head.next)
        if head.random:
            new_head.random = self.visited[head.random]        
        
        return new_head
        
head = Node(-1, None, None)
test = Solution()
print test.copyRandomList(head).val