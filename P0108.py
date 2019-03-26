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
        
        if not nums:
            return None  
        
        mid = len(nums)//2
        
        root = TreeNode(nums[mid])     
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
        
    
nums = [-10,-3,0,5,9]
test = Solution()
root = test.sortedArrayToBST(nums)     

s = [root]
ans = []
        
while s: 
    ans.append([n.val for n in s])   
    s = [child for n in s for child in [n.left, n.right] if child]     
         
print ans 