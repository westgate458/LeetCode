# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:14:33 2019

@author: Tianqi Guo
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # if we can reach the end of the list
        if not head or not head.next:
            # there is no cycle
            return False
        # if we have reached a visited node
        elif not head.next.val:
            # there is a cycle
            return True
        # if we have reached an un-visited node
        else:
            # mark this node visited
            head.val = None
            # move on to the next node
            return self.hasCycle(head.next)

