# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:38:13 2018

@author: Tianqi Guo
"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = 0       
        first_digit = ListNode(0)
        prev_digit = first_digit
        while (l1 != None) or (l2 != None) or (prev != 0):   
            if l1 != None:
                N1 = l1.val
                l1 = l1.next
            else:
                N1 = 0
            if l2 != None:
                N2 = l2.val
                l2 = l2.next
            else:
                N2 = 0
            N3 = N1 + N2 + prev
            prev = int(N3 >= 10)           
            this_digit = ListNode(N3 - prev * 10)
            prev_digit.next = this_digit
            prev_digit = this_digit
        return first_digit.next  
        
l1 = ListNode(5)
l2 = ListNode(5)

ans = Solution()
kk = ans.addTwoNumbers(l1,l2)
        
        
        
        
        
        
        
        