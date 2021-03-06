# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:26:01 2019

@author: Tianqi Guo
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution 1 beats 99.66%: binary search on each line
        # deal with trivial cases
        if not matrix or not matrix[0]:
            return False        
        # right limit: all numbers on the right of this location on this line is larger than target
        # so all numbers on the right of this location on lines below are also larger than target
        rr = len(matrix[0]) - 1        
        # continue searching while there are still numbers from beginning till rr
        # and there are more lines to go
        while rr >= 0 and matrix:
            # pop the top line for current search
            # for some reason it is faster than 
            # for row in matrix:
            row = matrix.pop(0)           
            # search limits
            l, r = 0, rr   
            # binary search in this limit
            while l <= r:
                # mid value
                m = (l + r)/2
                # if found, return YES
                if row[m] == target:
                    return True
                # update left search limit on this line
                elif row[m] < target:
                    l = m + 1
                # update right search limit on this line
                else:
                    r = m - 1
                    # also update the global right limit
                    rr = m - 1 
        # if all possibles are searched, then target does not exist
        return False
        
#        # Solution 2 beats 8.06%: binary search on borders, and update rectangular searching region
#        # subfunction for binary search
#        def b_search(nums,target): 
#            h, t = 0, len(nums)                
#            while h < t - 1:                  
#                m = int((h+t)/2)                   
#                if nums[m] == target:                    
#                    return m                
#                elif nums[m] > target:
#                    t = m
#                else:
#                    h = m 
#            return h        
#       
#        while matrix and matrix[0]:
#            
#            x = matrix[0]
#            y = [row[0] for row in matrix]        
#            x1 = b_search(x,target)
#            if x[x1] == target:
#                return True
#            y1 = b_search(y,target)
#            if y[y1] == target:
#                return True        
#            
#            x = matrix[-1]
#            y = [row[-1] for row in matrix] 
#            x2 = b_search(x,target)
#            if x[x2] == target:
#                return True
#            y2 = b_search(y,target)
#            if y[y2] == target:
#                return True  
#         
#            matrix = [row[x2+1:x1+1] for row in matrix[y2+1:y1+1]]
#                 
#        return False
       
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 14

test = Solution()
print(test.searchMatrix(matrix,target))
#        # search the closet value to the target
#        head = b_search(heads,target)
#        # determine what interval the target falls in
#        row, rmd = divmod(head, 2)
#        # if target is in heads list
#        if heads[head] == target:
#            # target found
#            return True
#        # if target is larger the last element in one row, 
#        # and smaller than the first element in the next row
#        elif rmd == 1:
#            # target is not in the matrix for sure
#            return False
#        # if target falls into the range of one row
#        else:    
#            # find its closest position in this row
#            clm = b_search(matrix[row],target)
#            # check if the closest value is equal to the target
#            return matrix[row][clm] == target