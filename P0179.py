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
        strs = [str(n) for n in nums]
        
        def helper(strs):
            
            d = defaultdict(list)
            for s in strs:
                d[s[0]] += [s]            
           
            strs_sorted = []
            for key in sorted(d.keys(), reverse = True):
                ss = [s[1:] for s in d[key] if s[1:]]   
                if ss != []:                        
                    ss = helper(ss)                    
                    i = 0                                     
                    while i < len(ss) and ss[i][0] > key:
                        i += 1                        
                    ss = [key + s for s in ss]
                    ss = ss[0:i] + [key] * (len(d[key]) - len(ss)) + ss[i:]
                else:
                    ss = d[key]
               
                strs_sorted += ss   
                
            return strs_sorted 
        
        ans = ''.join(helper(strs))
        if ans.lstrip('0') == '':
            return '0'
        else:
            return ans
            

        
     
nums = [10,2]
nums = [21, 2]
nums = [121,12]
nums = [3,30,34,5,9] 
nums = [0,0]
nums = [824,8247]
test = Solution()
print test.largestNumber(nums)