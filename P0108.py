# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:02:38 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None   

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # subfunction constructs BST from nums in range (l, r)
        def construct(l, r):   
            
            # if current range is empty return none
            if l > r:
                return None  
            
            # find midpoint
            mid = (l + r)//2
            
            # construct root node using the midpoint value
            root = TreeNode(nums[mid])     
            # construct left subtree recursively with values before midpoint
            root.left = construct(l, mid - 1)
            # construct right subtree recursively with values after midpoint
            root.right = construct(mid + 1, r)
            
            # return constructed root with its child subtrees
            return root
        
        # call subfunction and construct BST using all the numbers given
        return construct(0, len(nums)-1)
        
    
nums = [-10,-3,0,5,9]
test = Solution()
root = test.sortedArrayToBST(nums)     

s = [root]
ans = []
        
while s: 
    ans.append([n.val for n in s])   
    s = [child for n in s for child in [n.left, n.right] if child]     
         
print ans 