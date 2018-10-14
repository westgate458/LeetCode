# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:07:57 2018

@author: Tianqi Guo
"""

nums1 = []
nums2 = [1, 2, 3, 4]

if len(nums1) > len(nums2):
    A = nums2
    B = nums1
else:
    A = nums1
    B = nums2

l_1 = len(A)
l_2 = len(B)    
l_0 = l_1 + l_2
l_h = int(round(float(l_0)/2))

# search range from sR_l th to sR_r th
sR_l = 0
sR_r = l_1

while True:
    # numbers from A
    nfA = int((sR_l + sR_r + 1)/2)
    # numbers from B
    nfB = l_h - nfA
    # index of last number from A
    i = nfA - 1    
    # index of last number from B
    j = nfB - 1
    
#    if (nfA == 0) or (nfA == l_1):
#        break    
    if (nfB != l_2) and (nfA != 0) and (A[i] > B[j+1]):   
        # last number from A is larger than next in from B
        # search range of right set to the i th in A, i.e. the one before i
        sR_r = max(i, 0)
        continue
    if (nfA != l_1) and (A[i+1] < B[j]):
        # next number in A is smaller than last number from B
        # search range of left set to the i th in A, i.e. the one before i
        sR_l = min(i + 2, l_1)
        continue
    break

if l_0 % 2 == 0:    
    if nfA == 0:
        n_small = B[j]
    else:
        if nfB == 0:
            n_small = A[i]
        else:
            n_small = max(A[i], B[j])
    if nfA == l_1:
        n_large = B[j+1]
    else:
        if nfB == l_2:
            n_large = A[i+1]
        else:
            n_large = min(A[i+1], B[j+1])
    median = (float(n_small) + float(n_large))/2    
else:
    if nfA == 0:
        median = B[j]
    else:           
        median = max(A[i], B[j])
print(median)
        
    












