# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:15:58 2019

@author: Tianqi Guo
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # Solution 1 beats 98.85%: sliding window
        # deal with trivial case
        if not nums:
            return []        
        # max value of the first window
        c_max = max(nums[:k])
        # answer for all maxima
        ans = [c_max]        
        # slide window towards right
        for i in range(k,len(nums)):
            # if new number is larger then current max
            # or previous max has moved out from window
            if nums[i] > c_max or c_max == nums[i-k]:
                # update a new max
                c_max = max(nums[i-k+1:i+1])
            # record current max in this window
            ans.append(c_max)
        # return all maxima
        return(ans)
        
        
        # Solution 2 beats 27.13 %: deque
        from collections import deque
        if not nums:
            return []        
        q = deque()
        p = deque()        
        for i in range(k):
            q.append(nums[i])
            p.append(i)            
        ans = [max(q)]
        for i in range(k,len(nums)):            
            if q and i - p[0] >= k:
                q.popleft() 
                p.popleft()             
            while q and q[0] < nums[i]:
                q.popleft()
                p.popleft()             
            while q and q[-1] < nums[i]:
                q.pop()  
                p.pop()                 
            q.append(nums[i])
            p.append(i)            
            ans.append(max(q)) 
        return(ans)

nums = [1,3,-1,-3,5,3,6,7]
k = 3        
test = Solution()
print(test.maxSlidingWindow(nums, k))
        