# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 21:05:54 2018

@author: Tianqi Guo
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
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
                # add the current combo to the answer list
                self.ans.append(list(combo))
                return None
            
            # if remaining sum larger than zero
            # meaning more candidates need to be summed
            if remaining > 0:
                # how many candidates remaining
                l = len(candidates)
                # try each candidates in the list
                for i in range(l):
                    # if current candidate is a duplicated one
                    # skip it in current DFS level to avoid duplicates
                    if (i > 0) and (candidates[i] == candidates[i-1]):
                        continue
                    # if current number larger than remaining sum
                    if candidates[i] > remaining:
                        # break loop because add any remaining candidate will exceed target        
                        break
                    # if combo is empty or current candidate is not smaller than previous number in combo
                    if (not combo) or (candidates[i] >= combo[-1]): 
                        # remove current number from candidate list
                        num = candidates.pop(i)
                        # add current candidate to combo
                        combo.append(num)     
                        # continue DFS with updated condidate list, remaining sum and combo
                        DFS(candidates, remaining - num, combo)
                        # remove current number from combo, to try next candidate in next iteration
                        combo.pop(-1)     
                        # add the number back to candidate list
                        candidates.insert(i,num)
                        
        # list of combinations                     
        self.ans = []
        # sort candidates in ascending order
        candidates.sort()
        # start DFS with target as remaining and empty combo list
        DFS(candidates, target, list([]))
        # return list of combinations
        return self.ans

candidates = [10,1,2,7,6,1,5]
target = 8

test = Solution()
print(test.combinationSum2(candidates, target))
        
        
                    
                