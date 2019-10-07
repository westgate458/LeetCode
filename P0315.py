# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:43:28 2019

@author: Tianqi Guo
"""

# Tree node for BST
class Node(object):
    def __init__(self, val):
        # its own value
        self.val = val
        # its child trees
        self.left = None
        self.right = None    
        # count of numbers in its left child tree so far
        self.cc = 0
        
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        # deal with trivial case
        if not nums:
            return []    
        # number of nodes
        l = len(nums)
        # answer array, and the last number as the root
        counts, root = [0] * l, Node(nums[-1])    
        # we construct the tree from tail to head
        # so for each element, we already know how many numbers after it have smaller values
        for i in xrange(l-2, -1,-1):
            # we always start insertion from the root
            # cc is the counter that picks up number of smaller values along the path
            p, cc = root, 0    
            # continue binary search until target insertion position is found
            while True:
                # if current number is smaller than current node
                if nums[i] < p.val:
                    # then update node's counter
                    p.cc += 1
                    # if current node has left tree
                    if p.left:
                        # continue searching for insertion position
                        p = p.left
                    # if current node has no left tree
                    else:
                        # current number should be inserted here
                        p.left = Node(nums[i])
                        # record number of smaller values we picked along the path
                        counts[i] = cc
                        break
                # if current number is larger than or equal to current node
                else:   
                    # then all numbers that belong to current node's left child tree
                    # are smaller than current number
                    # and they all appear after current number in the original array
                    cc += p.cc 
                    # if current number is strictly larger than current node
                    if nums[i] > p.val:
                        # we pick up this one as well
                        cc += 1
                    # determine if we continue searching or insert current number here
                    if p.right:
                        p = p.right
                    else:                        
                        p.right = Node(nums[i])  
                        counts[i] = cc
                        break    
        # return the counts for all numbers
        return counts