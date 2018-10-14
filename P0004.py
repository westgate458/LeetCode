# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:07:57 2018

@author: Tianqi Guo
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # find the shorter list to start search
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2
        
        l_1 = len(A)
        l_2 = len(B)    
        l_0 = l_1 + l_2
        # the half length of the combined list
        # after which the median occurs
        l_h = int(round(float(l_0)/2))
        
        # search range from sR_l th to sR_r th
        # in the shorter list
        sR_l = 0
        sR_r = l_1
        
        # infinite loop until median is found
        # select first ith numbers from A and first jth numbers from B
        # to form the first half of the combined list -> C
        # the remaining numbers in A and B that not selected -> D
        # median is found if 
        # <all numbers in C are smaller than all numbers if D>
        # each time half the search range in A 
        # and include the first half in this range into C
        # then check if <condition> is satisfied
        while True:    
            
            # first half of the current search range from A to be included in C
            nfA = int((sR_l + sR_r + 1)/2)
            # numbers from B to be included in C
            nfB = l_h - nfA
            # index of last number from A in C
            i = nfA - 1    
            # index of last number from B in C
            j = nfB - 1
            
            # last number from A in C is larger than next number from B in D
            # <condition> not satisfied, numbers from A in C need to be smaller
            if (nfB != l_2) and (nfA != 0) and (A[i] > B[j+1]):                  
                # update search range of A, right set to the one before i
                sR_r = max(i, 0)
                continue
            # last number from B in C is larger than next number from A in D
            # <condition> not satisfied, numbers from A in C need to be larger
            if (nfA != l_1) and (A[i+1] < B[j]):
                # update search range of A, left set to the one after i
                sR_l = min(i + 2, l_1)
                continue
            # condition satisfied, terminate loop
            break
        
        # if even numbers in [A+B], median is mean of middle two
        # (largest number in C and smallest number in D)
        if l_0 % 2 == 0:    
            # determine the smaller number of the middle two
            # if no number from A is in C
            if nfA == 0:
                # smaller of middle two is the last in C from B
                n_small = B[j]
            else:
                # if no number from B is in C
                if nfB == 0:
                    # smaller of middle two is the last in C from A
                    n_small = A[i]
                else:
                    # if both numbers from A and B are in C
                    # the smaller number of middle two 
                    # is the larger one of last numbers from A and from B
                    n_small = max(A[i], B[j])
            # if all numbers in A are in C
            if nfA == l_1:
                # the larger number is the next one in D from B
                n_large = B[j+1]
            else:
                # if all numbers in B are in C
                if nfB == l_2:
                    # the larger number is the next one in D from A
                    n_large = A[i+1]
                else:
                    # if there are numbers from both A and B in D
                    # the larger number of the middle two
                    # is the smaller one of next numbers from A and from B
                    n_large = min(A[i+1], B[j+1])
            # take the mean of the middle two as the median
            median = (float(n_small) + float(n_large))/2    
        else:
            # if odd numbers in [A+B], median is middle one 
            # (largest number in C)
            # if no number from A in C
            if nfA == 0:
                # median is the largest from B in C
                median = B[j]
            else: 
                # if numbers from both A and B in C
                # median is the larger one of the last numbers from A and B
                median = max(A[i], B[j])
        
        # return result
        return(median)
        
test = Solution()

nums1 = []
nums2 = [1, 2, 3, 4]

print(test.findMedianSortedArrays(nums1,nums2))











