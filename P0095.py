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
        
        # subfunction that constructs the BST for number range (begin, end)
        def construct(begin, end): 
            
            # if current segment has already been constructed before
            if (begin, end) in self.dict:
                # return the constructed list of trees
                return self.dict[(begin, end)]
            # if begin point is even larger than end point
            elif begin > end:
                # No BST can be constructed in this range
                return [None]
            # if begin and end are the same
            elif begin == end:
                # a leaf is constructed
                return [TreeNode(begin)]
            # if there are more than 1 numbers in this range
            else:
                # list storing all possible BSTs for current segment
                root_list = []
                # make each number in current range as the node value
                # and use numbers before current number to construct left sub BST
                # and use numbers after current number to construct right sub BST
                # then for each combination from left BST and right BST
                for mid in range(begin,end+1):   
                    for left in construct(begin, mid-1):
                        for right in construct(mid+1, end):                            
                            # construct a node using current mid value
                            root = TreeNode(mid)
                            # take one from left and one from right as sub BSTs
                            root.left = left
                            root.right = right
                            # append current node to anwser list
                            root_list.append(root) 
                # store current BSTs for this particular number range
                # for future reference
                self.dict[(begin, end)] = root_list
            # return current BSTs for this particular number range
            return root_list
        
        # deal with trivial case
        if n == 0:
            return []
        else:
            # initialize the dictionary for BSTs of particular number ranges
            self.dict = {} 
            # construct all BSTs for the number range (1, n)
            return construct(1,n)    

n = 3
test = Solution()
root_list = test.generateTrees(n)  