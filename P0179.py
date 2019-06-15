# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:59:39 2019

@author: Tianqi Guo
"""
from collections import defaultdict
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        def helper(k, data):             
      
            ss_empty = [x[0] for x in data if x[1] < k+1]            
            ss = [x for x in data if x[1] >= k+1]   

            d = defaultdict(list)
            for s in ss:
                d[s[0][k]] += [s]  
  
            ss_sorted = []
            for key in sorted(d.keys(), reverse = True): 
                ss_sorted += helper(k + 1, d[key])               
          
            if ss_empty != []:
                i = 0                
                while i < len(ss_sorted) and (ss_sorted[i] + ss_empty[0] > ss_empty[0] + ss_sorted[i]):
                    i += 1                    
                ss_sorted = ss_sorted[:i] + ss_empty + ss_sorted[i:]
   
            return ss_sorted
        
        if sum(nums) == 0:
            return '0' 
        
        strs = [str(n) for n in nums]
        ls = [len(s) for s in strs]  

        return ''.join(helper(0, zip(strs,ls)))         
        
     
nums = [10,2]
nums = [21, 2]
nums = [3,30,34,5,9] 
nums = [6,7,76,77,78,8]
nums = [121,12]
nums = [0,0]
nums = [128,12]
nums = [2281,2162,2216,2132]
nums = [21, 2]
nums = [8308,830]
nums = [2281,2]

test = Solution()
print test.largestNumber(nums)