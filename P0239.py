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
        if not nums:
            return []        
        c_max = max(nums[:k])
        ans = [c_max]        
        for i in range(k,len(nums)):
            if nums[i] > c_max or c_max == nums[i-k]:
                c_max = max(nums[i-k+1:i+1])
            ans.append(c_max)
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
        