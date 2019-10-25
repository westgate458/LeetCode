# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:11:33 2019

@author: Tianqi Guo
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """        
        # Solution 1 beats 95.97%: looking backwards
        # start with 0 at 0
        ans = [0]
        # then we get ans for each number based on previous results
        for n in xrange(1,num+1):
            # x = n >> 1 is its half
            # y = n & 1 checks if the right most bit is 1
            # then current number is x * 2 + y
            # in binary is (x)_2 << 1 + y
            # so the number of 1's can be obtained as
            ans.append(ans[n>>1] + (n&1))     
        # return counts for all numbers
        return ans
    
        # Solution 2 beats 86.95%: looking forwards
        ans = [0]*(num+2)
        for n in xrange(num//2+1):
            ans[2*n],ans[2*n+1] = ans[n], ans[n]+1        
        return ans[:num+1]             