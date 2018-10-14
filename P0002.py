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
        
        # from previous digit
        prev = 0
        # initialize the linked list
        first_digit = ListNode(0)
        prev_digit = first_digit
        # coninue summation if not reaching the last digits
        while (l1 != None) or (l2 != None) or (prev != 0):   
            # if first number has not reached the end
            if l1 != None:
                # take current digit and point to next digit
                N1 = l1.val
                l1 = l1.next
            else:
                N1 = 0
            # same operation for the second number
            if l2 != None:
                N2 = l2.val
                l2 = l2.next
            else:
                N2 = 0
            # summation of current digit
            N3 = N1 + N2 + prev
            # if summation larger than 9
            prev = int(N3 >= 10)    
            # keep record of current digit and update the pointer
            this_digit = ListNode(N3 - prev * 10)
            prev_digit.next = this_digit
            prev_digit = this_digit
        # return the first node in the linked list
        return first_digit.next  
        
l1 = ListNode(5)
l2 = ListNode(5)

test = Solution()
ans = test.addTwoNumbers(l1,l2)
        
        
        
        
        
        
        
        