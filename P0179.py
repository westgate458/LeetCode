# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:59:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # Solution 1: using cmp in sorted
        # define a comparison function
        # it takes two value (two elements from the num list)
        # compare which one first gives a larger number if combined
        def com(s1, s2):
            # in order for the cmp to work this function need to 
            # 1) return positive value if we want s2 to be placed before s1 after sorted
            # 2) return negative value if we want s1 to be placed before s2 after sorted
            # since sorted at default sort elements in ascending order
            return 1 if s1 + s2 < s2 + s1 else -1      
        # for the given number list
        # 1) use map to convert to strs
        # 2) sort strings based on the comparison function defined
        # 3) join the sorted strings to form the largest number
        # 4) strip its proceeding 0's
        # 5) deal with trivial case of all numbers are 0
        return ''.join(sorted(map(str, nums), cmp = com)).lstrip('0') or '0' 
        
#        # Solution 2: divide and conquer, sorting dictionary keys  
#        from collections import defaultdict
#        def helper(k, data):                  
#            ss_empty = [x[0] for x in data if x[1] < k+1]            
#            ss = [x for x in data if x[1] >= k+1]   
#            d = defaultdict(list)
#            for s in ss:
#                d[s[0][k]] += [s]   
#            ss_sorted = []
#            for key in sorted(d.keys(), reverse = True): 
#                ss_sorted += helper(k + 1, d[key])                         
#            if ss_empty != []:
#                i = 0                
#                while i < len(ss_sorted) and (ss_sorted[i] + ss_empty[0] > ss_empty[0] + ss_sorted[i]):
#                    i += 1                    
#                ss_sorted = ss_sorted[:i] + ss_empty + ss_sorted[i:]   
#            return ss_sorted
#
#        strs = map(str, nums)
#        ls = map(len, strs)
#        return ''.join(helper(0, zip(strs,ls))).lstrip('0') or '0'          
        
     
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