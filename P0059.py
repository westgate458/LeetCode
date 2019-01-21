# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:59:32 2019

@author: Tianqi Guo
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        # index array corresponds to right, down, left, up
        di = [0,1,0,-1]
        dj = [1,0,-1,0]

        # initialize matrix with 0 as placehoders and -1 for boundaries
        matrix = [[-1]*(n+2)] + [[-1] + [0]*(n) + [-1] for x in range(n)] + [[-1]*(n+2)]

        # start with the first element and moving right
        i = 1
        j = 1
        d = 0
        # count of already inserted numbers
        c = 1
        
        # continue insertion until n^2
        while c <= n**2:
            
            # insert current number and move on
            matrix[i][j] = c
            c = c + 1
            
            # if next number along current direction is already inserted (or is on boundary)
            if matrix[i+di[d]][j+dj[d]] != 0:        
                # update direction and turn clockwise
                d = (d + 1)%4
            
            # indices of the next element
            i = i + di[d]
            j = j + dj[d]

        # return the center region of the matrix
        return [matrix[x][1:n+1] for x in range(1,n+1)]


n = 3
test = Solution()
print(test.generateMatrix(n))