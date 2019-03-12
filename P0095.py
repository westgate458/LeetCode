# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:34:56 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def construct(nums):           
        
            l = len(nums)
            root_list = []
            
            if l > 1:
                for i in range(l):    
                    nums_left = nums[:i]
                    nums_root = nums[i]
                    nums_right = nums[i+1:]  
                    
                    if nums_left:
                        list_left = construct(nums_left)
                    else:
                        list_left = [None]
                        
                    if nums_right:
                        list_right = construct(nums_right)   
                    else:
                        list_right = [None]                        
                                
                    for left in list_left:
                        for right in list_right:
                            root = TreeNode(nums_root)
                            root.left = left
                            root.right = right
                            root_list.append(root)
            else:
                root_list.append(TreeNode(nums[0]))
                
            return root_list
        
        if n == 0:
            return []
        else:
            return construct(range(1,n+1))
    

n = 0
test = Solution()
root_list = test.generateTrees(n)


            
        