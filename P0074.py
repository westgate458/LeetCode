# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:24:45 2019

@author: Tianqi Guo
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # subfunction for binary search
        def b_search(nums,target):
            
            # head pointer
            h = 0
            # tail pointer
            t = len(nums)    
            
            # search while two pointers have not met
            while h < t - 1:  
                # take midpoint
                m = int((h+t)/2)   
                # if target is found
                if nums[m] == target:
                    # return current index
                    return m
                # update search range according to midpoint value
                elif nums[m] > target:
                    t = m
                else:
                    h = m   
            # return index for closest value to target
            return h
        
        # deal with trivial case
        if not matrix:
            return False    
        # size of the matrix
        m = len(matrix)
        n = len(matrix[0])  
        # deal with trivial case
        if n == 0:
            return False
        # deal with special case: single column
        elif n == 1:
            heads = [matrix[i][0] for i in range(m)]
        # common case
        else:
            # heads list: take the first and the last numbers from each row
            heads = [matrix[i][0:n:n-1] for i in range(m)]
            # flatten the 2D list to 1D
            heads = [j for sub in heads for j in sub]          
        
        # search the closet value to the target
        head = b_search(heads,target)
        # determine what interval the target falls in
        row, rmd = divmod(head, 2)
        # if target is in heads list
        if heads[head] == target:
            # target found
            return True
        # if target is larger the last element in one row, 
        # and smaller than the first element in the next row
        elif rmd == 1:
            # target is not in the matrix for sure
            return False
        # if target falls into the range of one row
        else:    
            # find its closest position in this row
            clm = b_search(matrix[row],target)
            # check if the closest value is equal to the target
            return matrix[row][clm] == target
        
matrix = [[1],[3]]
target = 3
#matrix = [[1]]
#target = 1
test = Solution()
print test.searchMatrix(matrix,target)