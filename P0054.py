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
        
        if not matrix:
            return []
        
        di = [0,1,0,-1]
        dj = [1,0,-1,0]

        l1 = len(matrix)        
        l2 = len(matrix[0])        

        mark = 12345
        matrix.append([mark] * l2)
        matrix.insert(0,[mark] * l2)
        matrix = [[mark] + row + [mark] for row in matrix]

        i = 1
        j = 1
        d = 0
        ans = []
        while len(ans) != l1 * l2:

            ans.append(matrix[i][j])
            matrix[i][j] = mark    

            if matrix[i+di[d]][j+dj[d]] == mark:
                d = (d + 1)%4

            i = i + di[d]
            j = j + dj[d]

        return ans  


matrix = [[1,2,3,4,5,6,7,8,9,10],
          [11,12,13,14,15,16,17,18,19,20]]

test = Solution()
print(test.spiralOrder(matrix))