# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:02:49 2018

@author: Tianqi Guo
"""
import pdb
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def DFS(candidates, remaining, combo):
            
            if remaining == 0: 
                print(combo)
                
                if not combo in self.ans:
                    self.ans.append(list(combo))
                return None
            
            if remaining > 0:    
                if not combo:
                    last = 0
                else:
                    last = combo[-1]
                for num in candidates:
                    if num > remaining:
                        break
                    if num >= last: 
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
        
        
                    
                
        