# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:43:28 2019

@author: Tianqi Guo
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None        
        self.cc = 0
        
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        if not nums:
            return []    
        l = len(nums)
        counts, root = [0] * l, Node(nums[-1])       
        for i in xrange(l-2, -1,-1):
            p, cc = root, 0            
            while True:
                if nums[i] < p.val:
                    p.cc += 1
                    if p.left:
                        p = p.left
                    else:
                        p.left = Node(nums[i])
                        counts[i] = cc
                        break
                else:   
                    cc += p.cc 
                    if nums[i] > p.val:
                        cc += 1
                    if p.right:
                        p = p.right
                    else:                        
                        p.right = Node(nums[i])  
                        counts[i] = cc
                        break    
        
        return counts