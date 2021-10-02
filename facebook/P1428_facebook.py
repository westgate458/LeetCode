# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """        
        r, c = binaryMatrix.dimensions()
        i, j, res = 0, c-1, -1       
        while (i<r and j>=0):
            if binaryMatrix.get(i, j):
                res = j
                j -= 1
            else:
                i += 1
        return res