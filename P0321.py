# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:27:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # Sub-problem 1: k-length max number from nums
        def pick_k(nums, k):      
            # counter: digits from nums that can be discarded
            n = len(nums)-k
            # digits we picked
            picked = []
            # check each digit in nums
            for num in nums:
                # greedy rule: 
                # if previous digit in picked is smaller than current digit
                # and we can discard more digits                
                while picked and num > picked[-1] and n:
                    # then we discard previous digit
                    picked.pop()
                    # and update counter
                    n -= 1
                # place current digit in its proper position
                picked.append(num)
            # only return first k digits, in case len(nums) > k
            return picked[:k]
        
        # Sub-problem 2: max number from merging two nums, all digits need to be used
        def merge(nums1, nums2):
            # p1, p2: pointers to current digits to consider in two numbers
            # l1, l2: lengths of two nums
            # merged: the resulting merged max number
            p1, p2, l1, l2, merged = 0, 0, len(nums1), len(nums2), []            
            # continue comparing if more digits to consider in both nums
            while p1 < l1 and p2 < l2:
                # pick the larger one from the two digits, and update pointer
                if nums1[p1:] >= nums2[p2:]:
                    merged.append(nums1[p1])
                    p1 += 1
                else:
                    merged.append(nums2[p2])
                    p2 += 1                 
            # add rest digits to merged number
            merged += nums1[p1:] + nums2[p2:]

            return merged
        
        # lengths of two numbers
        l1, l2 = len(nums1), len(nums2)        
        # minimum and maximum number of digits to be picked from nums1
        # ans: the max number formed
        min_from_nums1, max_from_nums1, ans = max(0, k - l2), min(l1,k), [0] * k         
        # try picking different number of digits from two nums 
        for k1 in range(min_from_nums1, max_from_nums1 + 1):  
            # pick_k(nums1, k1): max number from picking k1 digits in nums1
            # pick_k(nums2, k - k1): max number from picking k-k1 digits in nums2
            # then merge the two to have the max number of length k
            # finally update the answer
            ans = max(ans, merge(pick_k(nums1, k1), pick_k(nums2, k - k1)))
        return ans
                    
                
            