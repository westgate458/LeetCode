# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:23:57 2019

@author: westg_000
"""

# Solution 1 beats  47.71%: naive segment tree
class Node(object):
    def __init__(self, l, r, start, mid, end, val):        
        self.l = l
        self.r = r
        self.start = start
        self.mid = mid
        self.end = end
        self.val = val
        
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """  
        def construct(start, end):            
            if start > end:
                return None
            if start == end:
                return Node(None, None, start, start, end, nums[start])           
            mid = (start + end)//2
            l, r = construct(start, mid), construct(mid+1, end)
            return Node(l, r, start, mid, end, l.val + r.val)
        
        self.root = construct(0, len(nums)-1)       
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        def updateVal(n):  
            if n.start == n.end:
                n.val = val                
            else: 
                if i <= n.mid:
                    updateVal(n.l)
                else:
                    updateVal(n.r)
                n.val = n.l.val + n.r.val
        
        updateVal(self.root)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def getSum(n, i, j):           
            if n.start == i and j == n.end:
                return n.val        
            elif j <= n.mid:
                return getSum(n.l, i, j)
            elif i > n.mid:
                return getSum(n.r, i, j)
            else:
                return getSum(n.l, i, n.mid) + getSum(n.r, n.mid+1, j)
    
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
