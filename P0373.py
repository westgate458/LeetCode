# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:42:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Solution 1 beats 93.26%: heapsort
        # deal with trivial cases
        if not nums1 or not nums2:
            return []
        # initialize heap and result of k pairs
        heap, res = [], []
        # length of current sums, and lengths of two arrays
        l, l1, l2 = 0, len(nums1), len(nums2)
        # push the smallest sum into heap, and their indices
        heapq.heappush(heap, (nums1[0]+nums2[0],0,0))
        # if there are more sums in the heap and we have not obtained all k pairs
        while heap and l < k:
            # take the smallest sum in the heap
            _, i, j = heapq.heappop(heap)
            # record current pair
            res.append([nums1[i],nums2[j]])
            # update length of sums
            l += 1       
            # move on to next pairs
            # to avoid duplicates, only move to next i when j is 0
            if j == 0 and i + 1 < l1:
                heapq.heappush(heap, (nums1[i+1]+nums2[j],i+1,j))
            # move on to next j
            if j + 1 < l2:
                heapq.heappush(heap, (nums1[i]+nums2[j+1],i,j+1))
        # return all pairs
        return res
    
        # Solution 2 beats 23.90%: naive 1-liner
        return(sorted([(x, y) for x in nums1[:k] for y in nums2[:k]],key=sum)[:k])