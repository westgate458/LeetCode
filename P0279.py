# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:49:30 2019

@author: Tianqi Guo
"""

# Solution 1 beats 97.39%: cheating DP
class Solution(object):
    _ans = [0] 
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """        
        squares = [x**2 for x in range(1,int(n**0.5)+1)]
        ans = self._ans        
        while len(ans) <= n:
            num = len(ans)        
            c = num - 1
            for square in squares:               
                if square > num:
                    break
                elif ans[num-square] < c:
                    c = ans[num-square]
            ans += [c + 1]       
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