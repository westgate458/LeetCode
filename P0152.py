# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:50:31 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_p, max_p, ans = 1, 1, None
        for num in nums:                 
            p1 = max_p * num
            p2 = min_p * num     
            min_p = min(num, p1, p2)
            max_p = max(num, p1, p2)
            ans = max(max_p,ans)            
#            if num >= p1:                
#                if p1 >= p2:
#                    max_p, min_p = num, p2
#                elif num >= p2:
#                    max_p, min_p = num, p1
#                else:
#                    max_p, min_p = p2, p1
#            else:                
#                if num >= p2:
#                    max_p, min_p = p1, p2   
#                elif p1 > p2:
#                    max_p, min_p = p1, num                    
#                else:
#                    max_p, min_p = p2, num                         
#            if max_p > ans:            
#                ans = max_p
        return ans

tests = [[2,3,-2,4],
[-1,-2,-9,-6],
[-2,0,-2,-2],
[-2,0,-1],
[3,-1,4],
[-2]
]

test = Solution()
for nums in tests:
    print nums, test.maxProduct(nums)

