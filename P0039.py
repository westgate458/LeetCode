# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:02:49 2018

@author: Tianqi Guo
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # a subfunction that find all combinations by DFS
        def DFS(candidates, remaining, combo):
            
            # if remaining sum is zero
            # meaning current combination sums to target
            if remaining == 0:
                # add current combination to answer list
                self.ans.append(list(combo))
                return None
            
            # if remaining sum larger than zero
            # meaning more candidates need to be summed
            if remaining > 0:
                # for each candidate
                for num in candidates:
                    # if current number larger than remaining sum
                    if num > remaining:
                        # break loop because add any remaining candidate will exceed target                        
                        break
                    # if combo is empty or current candidate is not smaller than previous number in combo
                    # this ensures no duplicate combo will exist in final answer list
                    if (not combo) or (num >= combo[-1]): 
                        # add current candidate to combo
                        combo.append(num)
                        # continue DFS with the same condidate list, but new remaining sum and new combo
                        DFS(candidates, remaining - num, combo)
                        # remove current candidate from combo, to try next candidate in next iteration
                        combo.pop(-1)      
        
        # list of combinations                
        self.ans = []
        # sort candidates in ascending order
        candidates.sort()
        # start DFS with target as remaining and empty combo list
        DFS(candidates, target, list([]))
        # return list of combinations
        return self.ans

candidates = [4,2,8]
target = 8

test = Solution()
print(test.combinationSum(candidates, target))
        
        
                    
                
        