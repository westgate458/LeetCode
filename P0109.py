# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:47:42 2019

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

   
class Solution(object):    
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        def sortedArrayToBST(l, r):
               
            if l > r:
                return None  

            mid = (l + r)/2        
            root = TreeNode(nums[mid])  

            if l == r:
                return root

            root.left = sortedArrayToBST(l, mid - 1)
            root.right = sortedArrayToBST(mid + 1, r)

            return root    
        
        return sortedArrayToBST(0, len(nums)-1)
