# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:23:57 2019

@author: westg_000
"""

# Solution 1 beats  47.71%: naive segment tree
# class of tree nodes
class Node(object):    
    def __init__(self, l, r, start, mid, end, val):        
        # the node has following attributes
        # left and right child trees
        self.l = l        
        self.r = r
        # current sum (val) is from start till end in nums array
        # mid is the split point where left tree is [start, mid], right tree is [mid+1, end]
        self.start = start
        self.mid = mid
        self.end = end
        self.val = val
        
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """  
        # subfunction to construct the tree
        def construct(start, end):            
            # from start to end in nums array
            # if we have gone beyond the leaf
            if start > end:
                # no need to construct further
                return None
            # if current node is a leaf
            if start == end:
                # construct current node with no child trees
                # start, mid, end are the same, and sum is a single number                
                return Node(None, None, start, start, end, nums[start])   
            # if current node is a not a leaf
            # take the mid
            mid = (start + end)//2
            # construct left and right child trees first
            l, r = construct(start, mid), construct(mid+1, end)
            # construct current node with the child trees, and sums from them
            return Node(l, r, start, mid, end, l.val + r.val)
        # start construct from the root, i.e. node corresponds to the whole range
        self.root = construct(0, len(nums)-1)       
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        # subfunction to update a single value
        def updateVal(n):  
            # if current leaf is the one to update
            if n.start == n.end:
                # change the value
                n.val = val                
            # if current node is a segment sum
            else: 
                # first update the subtree the updated number belongs to                
                if i <= n.mid:
                    updateVal(n.l)
                else:
                    updateVal(n.r)
                # update the segment sum at current level
                n.val = n.l.val + n.r.val
        # start updating the whole tree from top
        updateVal(self.root)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # subfunction to get the sum of the range
        def getSum(n, i, j):           
            # if the range is current leaf
            if n.start == i and j == n.end:
                # simply return the single value
                return n.val        
            # if current range covers more than one number
            # we have three scenarios
            # 1) the whole range falls into left tree
            elif j <= n.mid:
                # get the sum from the left tree
                return getSum(n.l, i, j)
            # 2) the whole range falls into right tree
            elif i > n.mid:
                # get the sum from the right tree
                return getSum(n.r, i, j)
            # 3) the whole range covers both left and right trees
            else:
                # get sums from the two trees and take the sum of the two
                return getSum(n.l, i, n.mid) + getSum(n.r, n.mid+1, j)
        # get sum from the root top-down
        return getSum(self.root, i, j)


## Solution 2 beats 17.28%: straight forward summation
#class NumArray(object):
#
#    def __init__(self, nums):
#        """
#        :type nums: List[int]
#        """        
#        self.nums = nums
#
#    def update(self, i, val):
#        """
#        :type i: int
#        :type val: int
#        :rtype: None
#        """
#        self.nums[i] = val        
#
#    def sumRange(self, i, j):
#        """
#        :type i: int
#        :type j: int
#        :rtype: int
#        """
#        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
