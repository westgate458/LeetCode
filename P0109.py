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
        
        # convert linked list to regular list
        nums = []        
        while head:
            nums.append(head.val)
            head = head.next
        
        # subfunction constructs BST from nums in range (l, r)
        def sortedArrayToBST(l, r):
            
            # if current range is empty return none
            if l > r:
                return None  

            # find midpoint
            mid = (l + r)/2     
            # construct root node using the midpoint value
            root = TreeNode(nums[mid])  
            
            # if only one element then return constructed root
            if l == r:
                return root

            # construct left subtree recursively with values before midpoint
            root.left = sortedArrayToBST(l, mid - 1)
            # construct right subtree recursively with values after midpoint
            root.right = sortedArrayToBST(mid + 1, r)
            
            # return constructed root with its child subtrees
            return root    
        
        # call subfunction and construct BST using all the numbers given
        return sortedArrayToBST(0, len(nums)-1)
