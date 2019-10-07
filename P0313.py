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
        # initialize all ugly number as 1
        ans = [1] * n
        # most recent prime multiplied to get each ugly number
        last_prime = [1] * n   
        # for each prime number, position of its last multiplier in the ugly array
        ps = [0] * len(primes)   
        # we record each candidate in a heap
        candidates = []        
        # first add all primes into the candidate heap, together with the indices
        for idx, prime in enumerate(primes):
            heapq.heappush(candidates, (prime, idx))
        # now generate all ugly numbers as ugly = p1^e1 * p2^e2 * ... * pn^en
        for i in xrange(1,n): 
            # retrieve the smallest candidate from the heap, 
            # together with the index for the most recent prime number
            ans[i], idx = heapq.heappop(candidates)   
            # most recent prime multiplied to get this ugly number
            last_prime[i] = primes[idx]
            # now this most recent prime needs to multiply next ugly number to get new candidate
            ps[idx] += 1            
            # to avoid duplicate, we look for the next ugly number,
            # whose most recent prime-factor is smaller than or equal to current prime number
            while last_prime[ps[idx]] > primes[idx]:   
                ps[idx] += 1 
            # push new candidate, and current prime index into heap
            heapq.heappush(candidates, (ans[ps[idx]] * primes[idx], idx))        
        # last element in the answer list is the n-th ugly number
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