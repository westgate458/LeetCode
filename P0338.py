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
        ans = [0]
        for n in xrange(1,num+1):
            ans.append(ans[n>>1] + (n&1))     
        return ans
    
        # Solution 2 beats 86.95%: looking forwards
        ans = [0]*(num+2)
        for n in xrange(num//2+1):
            ans[2*n],ans[2*n+1] = ans[n], ans[n]+1        
        return ans[:num+1]             