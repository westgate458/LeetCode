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
        
        if not head or not head.next:
            return False
        elif not head.next.val:
            return True
        else:
            head.val = None
            return self.hasCycle(head.next)

