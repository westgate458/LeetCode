# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        for j in range(1,n):               
            if knows(i,j):
                i = j  
            
        for j in range(i):
            if knows(i,j): return -1
        
        for j in range(n):
            if knows(j,i)==0: return -1     
        
        return i
        
        
                    