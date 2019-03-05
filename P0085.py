# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:06:55 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # deal with trivial cases
        if not matrix or not matrix[0]:
            return 0
        
        # number of elements for each row
        n = len(matrix[0])        
        
        # initialize areas so far with 0's
        areas = [0]* (n+1)
        # maximum area so far
        area = 0
        
        # examine each row from top to bottom
        for row in matrix:
            # update the areas according to elements in current row
            # if it's non-zero add corresponding value in areas by 1
            # if it's zero set corresponding value in areas as 0
            # pad areas at the end with one extra 0 for following area calculation
            areas = [areas[i] + 1 if row[i] == '1' else 0 for i in range(n)] + [0]
            # indices of the 'increasing height list'             
            # initialize with -1 so the padded 0 at the end could be used twice
            
            # convert this problem to P0084
            ps = [-1]            
            # traverse the height list
            for p in range(n+1):   
                # if the current height smaller than 
                # previous height in the 'increasing height list'
                while areas[p] < areas[ps[-1]]:
                    # previous height in the 'increasing height list'
                    # can not be contained in an area starting from current p
                    # remove its index from the 'increasing height list'
                    pp = ps.pop()        
                    # the area forms with its height
                    # spans between two heights just lower than it
                    # the left limit is the current last index in the 'increasing height list'
                    # the right limit is the current p
                    # calculate the area
                    area_pp = (p - ps[-1] - 1) * areas[pp]
                    # update the maximum area so far
                    if area_pp > area:
                        area = area_pp 
                
                # place current index into the increasing height list
                # after all previous heights higher than current one
                # have been removed from the list
                ps.append(p)
                
        # return the maximum area
        return area

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

test = Solution()
print test.maximalRectangle(matrix)