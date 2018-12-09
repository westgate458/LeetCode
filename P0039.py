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
        
        def DFS(candidates, remaining, combo):
            
            if remaining == 0:
                if not combo in self.ans:
                    self.ans.append(list(combo))
                return None
            
            if remaining > 0:
                for num in candidates:
                    if num > remaining:
                        break
                    if (not combo) or (num >= combo[-1]): 
                        combo.append(num)
                        DFS(candidates, remaining - num, combo)
                        combo.pop(-1)      
                        
        self.ans = []
        candidates.sort()
        DFS(candidates, target, list([]))
        return self.ans

candidates = [4,2,8]
target = 8

test = Solution()
print(test.combinationSum(candidates, target))
        
        
                    
                
        