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
        if (1 + maxChoosableInteger)*maxChoosableInteger//2 < desiredTotal: return False
        self.dp = {}
        def makeMove(cur, total):  
            if cur in self.dp: return self.dp[cur]            
            for num in range(maxChoosableInteger,0,-1):     
                bit = 1 << num
                if not (bit & cur) and (num + total >= desiredTotal or (not makeMove(cur | bit, num + total))):                                   
                    self.dp[cur] = True
                    return True 
            self.dp[cur] = False
            return False     
        return makeMove(0, 0)