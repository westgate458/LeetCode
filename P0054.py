# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 19:42:08 2019

@author: Tianqi Guo
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # deal with trivial case
        if not matrix:
            return []
        
        # index array corresponds to right, down, left, up
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        
        # dimensions of the matrix
        l1 = len(matrix)        
        l2 = len(matrix[0])        
        
        # arbitraty mark that indicates already-output numbers
        mark = 12345
        # pad the matrix with marks
        matrix.append([mark] * l2)
        matrix.insert(0,[mark] * l2)
        matrix = [[mark] + row + [mark] for row in matrix]
        
        # start with the first element and moving right
        i = 1
        j = 1
        d = 0
        # answer of the output numbers
        ans = []
        # continue traverse until all elements are output
        while len(ans) != l1 * l2:
            # add current number to the answer array
            ans.append(matrix[i][j])
            # mark current position as already visited
            matrix[i][j] = mark    
            # if next number along current direction is already output (or is on boundary)
            if matrix[i+di[d]][j+dj[d]] == mark:
                # update direction and turn clockwise
                d = (d + 1)%4
            # indices of the next element
            i = i + di[d]
            j = j + dj[d]
        
        # return the numbers in spiral order
        return ans  


matrix = [[1,2,3,4,5,6,7,8,9,10],
          [11,12,13,14,15,16,17,18,19,20]]

test = Solution()
print(test.spiralOrder(matrix))