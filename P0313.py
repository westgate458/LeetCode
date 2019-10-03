# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:50:22 2019

@author: westg
"""

# Solution 1 beasts 99.49%: keep all candidates in a heap
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """        
        ans = [1] * n
        last_prime = [1] * n        
        ps = [0] * len(primes)   
        candidates = []        
        for idx, prime in enumerate(primes):
            heapq.heappush(candidates, (prime, idx))
        
        for i in xrange(1,n): 
            ans[i], idx = heapq.heappop(candidates)   
            last_prime[i] = primes[idx]
            ps[idx] += 1
            while last_prime[ps[idx]] > primes[idx]:   
                ps[idx] += 1 
            heapq.heappush(candidates, (ans[ps[idx]] * primes[idx], idx))        
        return ans[-1]

## Solution 2 beats 57.65%: adapted from P0264
#class Solution(object):
#    def nthSuperUglyNumber(self, n, primes):
#        """
#        :type n: int
#        :type primes: List[int]
#        :rtype: int
#        """        
#        ans = [1] * n
#        l = len(primes)   
#        ps = [0] * l
#        candidates = [1] * l 
#        for i in xrange(1,n):            
#            for p in xrange(l):                
#                while ans[ps[p]] * primes[p] <= ans[i-1]:   
#                    ps[p] += 1      
#                candidates[p] = ans[ps[p]] * primes[p]
#            ans[i] = min(candidates)
#        return ans[-1]