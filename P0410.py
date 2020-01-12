# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:38:24 2020

@author: Tianqi Guo
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """          
        # Solution 1 beats 95.52%: binary search
        # we search for the largest interval sum of interest
        # the smallest possible value is from splitting the array by each one number
        # the largest possible value is we use all number as one interval
        l, r = max(nums), sum(nums)        
        # continue searching until two ends meet
        while l < r:
            # we take the middle value
            mid = (l+r)//2            
            # group_num: how many intervals we end up with if mid is the largest interval sum
            # group_sum: running sum of current interval
            group_num, group_sum = 1, 0                 
            # calculate the running sums of each interval
            for num in nums:
                # update sum
                group_sum += num
                # if current sum exceeds target sum
                if group_sum > mid:
                    # current number marks the start of a new interval
                    group_sum = num
                    # update number of intervals
                    group_num += 1            
            # if we end up with more intervals than desired
            if group_num > m:
                # it means current mid is too small, we search the right half
                l = mid + 1                
            # the opposite if mid is too large
            else:
                r = mid
        # now l = r = the desired largest sum among all split intervals
        return l
    
        # Solution 2 beats 37.65%: DFS + memorization
        l = len(nums)      
        d = [[0]*(m+1) for _ in xrange(l)]        
        sums = [0]*(l+1) 
        for i in xrange(l):
            sums[i+1] = sums[i] + nums[i]        
        def DFS(i, m):            
            if m == 1:                
                d[i][m] = sums[-1]-sums[i]                         
            elif d[i][m] == 0:
                d[i][m] = float('inf')    
                for k in xrange(i,l-m+1):    
                    left = sums[k+1]-sums[i]
                    if left < d[i][m]:
                        right = DFS(k+1,m-1)
                        d[i][m] = min(d[i][m], max(left, right))      
                    else:
                        break   
            return d[i][m]
        return(DFS(0,m))    