# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:49:30 2019

@author: Tianqi Guo
"""

# Solution 1 beats 97.39%: cheating DP
class Solution(object):
    # somehow, define this as a global variable is much faster
    _ans = [0] 
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """        
        # all square numbers needed are the ones smaller than n
        squares = [x**2 for x in range(1,int(n**0.5)+1)]
        # pointer to the global variable
        ans = self._ans       
        # somehow, using while loop is much faster than for loop
        while len(ans) <= n:
            # somehow, taking length of the number list as current number
            # is much faster than num += 1
            num = len(ans)        
            # find the best previous status, i.e. the minimal number of squares
            c = num - 1
            # try each square
            for square in squares:               
                # stop trial when current square is larger than current number
                if square > num:
                    break
                # update optimal status
                elif ans[num-square] < c:
                    c = ans[num-square]
            # record optimal status for current number
            ans += [c + 1]       
        # somehow return the last number ans[-1] does not work
        return(ans[n])

# Solution 2 beats 63.50%: regular DP
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """        
        squares = [x**2 for x in range(1,int(n**0.5)+1)]
        ans = [x for x in range(n+1)] 
        for num in range(1, n+1):
            for square in squares:               
                if square > num:
                    break
                elif ans[num-square] + 1 < ans[num]:
                    ans[num] = ans[num-square] + 1        
        return(ans[-1])
        
n = 12
test = Solution()
print(test.numSquares(n))