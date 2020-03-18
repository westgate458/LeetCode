# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:30:09 2020

@author: Tianqi Guo
"""

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # deal with trivial case: desired total is not reachable
        if (1 + maxChoosableInteger)*maxChoosableInteger//2 < desiredTotal: return False
        # dp[i] status: current player can win with i numbers taken already
        # number k from [1,maxChoosableInteger] is taken if k-th bit in i is 1
        self.dp = {}
        # check if current player can win
        def makeMove(cur, total):  
            # if current status has been calculated before
            # directly retrieve the cached dp result
            if cur in self.dp: return self.dp[cur]    
            # try each number in the range [1,maxChoosableInteger]
            # we start from large ones since it speeds up the DFS
            for num in range(maxChoosableInteger,0,-1):  
                # encode current number
                bit = 1 << num
                # check three things:
                # 1) if current number is already taken -> move on to next one
                # 2) if current player can already win with current number -> mark winner and return
                # 3) if after current player taking this number, opponent can't win -> mark winner and return
                if not (bit & cur) and (num + total >= desiredTotal or (not makeMove(cur | bit, num + total))):                                   
                    self.dp[cur] = True
                    return True 
            # if after all available numbers are tried, current player cannot win
            self.dp[cur] = False
            # the opponent wins
            return False     
        # start DFS with 1st player, with all numbers available, and accumulative sum 0
        return makeMove(0, 0)