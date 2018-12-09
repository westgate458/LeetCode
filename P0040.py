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
        def DFS(candidates, remaining, combo):
            
            if remaining == 0:                
                if not combo in self.ans:
                    self.ans.append(list(combo))
                return None
            
            if remaining > 0:
                l = len(candidates)
                for i in range(l):
                    if candidates[i] > remaining:
                        break
                    if (not combo) or (candidates[i] >= combo[-1]): 
                        combo.append(candidates[i])                        
                        num = candidates.pop(i)
                        DFS(candidates, remaining - num, combo)
                        combo.pop(-1)     
                        candidates.insert(i,num)
                        
        self.ans = []
        candidates.sort()
        DFS(candidates, target, list([]))
        return self.ans

candidates = [2,5,2,1,2]
target = 5

test = Solution()
print(test.combinationSum2(candidates, target))
        
        
                    
                