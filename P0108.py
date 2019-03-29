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
        
        def construct(l, r):   
        
            if l > r:
                return None  

            mid = (l + r)//2

            root = TreeNode(nums[mid])     
            root.left = construct(l, mid - 1)
            root.right = construct(mid + 1, r)

            return root
        
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