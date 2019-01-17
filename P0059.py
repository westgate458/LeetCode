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
        di = [0,1,0,-1]
        dj = [1,0,-1,0]

        matrix = [[-1]*(n+2)] + [[-1] + [0]*(n) + [-1] for x in range(n)] + [[-1]*(n+2)]

        i = 1
        j = 1
        d = 0
        c = 1

        while c <= n**2:

            matrix[i][j] = c
            c = c + 1

            if matrix[i+di[d]][j+dj[d]] != 0:        
                d = (d + 1)%4

            i = i + di[d]
            j = j + dj[d]


        return [matrix[x][1:n+1] for x in range(1,n+1)]


n = 3
test = Solution()
print(test.generateMatrix(n))