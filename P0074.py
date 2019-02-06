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
        def b_search(nums,target):
            h = 0
            t = len(nums)             
            while h < t - 1:                
                m = int((h+t)/2)                    
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    t = m
                else:
                    h = m           
            return h
        
        if not matrix:
            return False        
        m = len(matrix)
        n = len(matrix[0])        
        if n == 0:
            return False
        elif n == 1:
            heads = [matrix[i][0] for i in range(m)]
        else:
            heads = [matrix[i][0:n:n-1] for i in range(m)]
            heads = [j for sub in heads for j in sub]          
        
        head = b_search(heads,target)
        row, rmd = divmod(head, 2)
        if heads[head] == target:
            return True
        elif rmd == 1:
            return False
        else:    
            clm = b_search(matrix[row],target)
            return matrix[row][clm] == target
        
matrix = [[1],[3]]
target = 3
#matrix = [[1]]
#target = 1
test = Solution()
print test.searchMatrix(matrix,target)