# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:09:03 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0        
        # Solution 1: bucket sorting
        max_num, min_num = max(nums), min(nums)
        if max_num == min_num:
            return 0        
        interval = (max_num - min_num)//len(nums) + 1
        buckets = [[None, None] for x in xrange((max_num - min_num)//interval+1)]        
        for num in nums:
            bucket = buckets[(num - min_num)//interval]
            if not bucket[0] or bucket[0]>num:
                bucket[0] = num
            if not bucket[1] or bucket[1]<num:
                bucket[1] = num                
        buckets = [bucket for bucket in buckets if bucket[0]]
        max_intra = max([bucket[1] - bucket[0] for bucket in buckets])
        max_inter = max([buckets[i][0] - buckets[i-1][1] for i in xrange(1,len(buckets))])        
        return max(max_intra,max_inter)
        
#        # Solution 2: cheating
#        nums.sort()
#        return max([x-y for (x,y) in zip(nums[1:],nums[0:-1])])
        
nums = [3,6,9,1]
nums = [2,99999999]
test = Solution()
print test.maximumGap(nums)