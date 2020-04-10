# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:48:07 2020

@author: Tianqi Guo
"""

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        
        # Solution 1 beats 99.47%: bottom-up dp
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]        
        for i in range(n): dp[i][i] = (nums[i],0)
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i + l - 1
                sl1, sl2 = dp[i+1][j] 
                sr1, sr2 = dp[i][j-1]
                dp[i][j] = (nums[i] + sl2, sl1) if nums[i] + sl2 >= nums[j] + sr2 else (nums[j] + sr2, sr1)                            
        return dp[0][-1][0] >= dp[0][-1][1]
        
        # Solution 2 beats 47.34%: top-bottom dp
        self.dp = {}
        def makeMove(i, j): 
            if (i,j) not in self.dp:
                if i == j:
                    self.dp[(i,j)] = (nums[i], 0) 
                else:                
                    sl1, sl2 = makeMove(i+1, j)
                    sr1, sr2 = makeMove(i, j-1)
                    if nums[i] + sl2 >= nums[j] + sr2:
                        self.dp[(i,j)] = (nums[i] + sl2, sl1)
                    else:
                        self.dp[(i,j)] = (nums[j] + sr2, sr1)
            return self.dp[(i,j)]
        s1, s2 = makeMove(0, len(nums)-1)
        return s1 >= s2
        
        # Solution 3 beats 28.72%: adaptation from P0464
        self.dp = {}
        def makeMove(i, j, picked_1, picked_2, total_1, total_2, player):  
            if (picked_1, picked_2) not in self.dp:
                self.dp[(picked_1, picked_2)] = False
                if i == j:                
                    if player == 1:
                        self.dp[(picked_1, picked_2)] = total_1 + nums[i] >= total_2                                 
                    else:
                        self.dp[(picked_1, picked_2)] = total_1 >= total_2 + nums[i] 
                else:
                    pick_i, pick_j = 1 << i, 1 << j                
                    if player == 1:                    
                        self.dp[(picked_1, picked_2)] = makeMove(i+1, j, picked_1|pick_i, picked_2, total_1+nums[i], total_2, 2) or makeMove(i, j-1, picked_1|pick_j, picked_2, total_1+nums[j], total_2, 2)             
                    else:                    
                        self.dp[(picked_1, picked_2)] = makeMove(i+1, j, picked_1, picked_2|pick_i, total_1, total_2+nums[i], 1) and makeMove(i, j-1, picked_1, picked_2|pick_j, total_1, total_2+nums[j], 1) 
            return self.dp[(picked_1, picked_2)]
        return makeMove(0, len(nums)-1, 0, 0, 0, 0, 1)