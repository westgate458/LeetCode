# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:51:58 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # start from 1
        cur = 1       
        # k is the remaining number counts
        k -= 1
        # we stop loop when k is 0
        while k > 0:
            # left and right: left-most and right-most numbers of current level
            # step: the number of numbers between current node the the node to the right
            left, right, step = cur, cur + 1, 0            
            # we continue looking at child levels until the left-most number is larger than
            # the max number n, i.e. the denary tree ends at previous level
            while left <= n:
                # if we want to move to next node to the right
                # we need to count all numbers at current level
                # whether current level is full depends on if the right-most number is smaller than n
                step += min(right, n+1) - left 
                # move on to next level
                left, right = 10*left, 10*right                
            # if there are enough numbers between current node and the node to the right
            if step <= k:
                # we count all the numbers and update remaining k
                k -= step
                # move on to the next node (the denary tree on the right)
                cur += 1
            # if we can not make to the next node, i.e. the k-th number is within current denary tree
            # but at lower levels
            else:
                # we only count current node, update k
                k -= 1
                # and move on to the child node
                cur *= 10
        # when k = 0 we reached the target number
        return(cur)