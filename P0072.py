# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:02:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)

        steps = [range(l2+1)] + [[x]+[0]* l2 for x in range(1,l1+1)]

        for m in range(1,l1+1):
            for n in range(1,l2+1):        
                if word1[m-1] == word2[n-1]:
                    steps[m][n] = steps[m-1][n-1]
                else:
                    steps[m][n] = min(steps[m-1][n],steps[m][n-1],steps[m-1][n-1]) + 1

        return steps[-1][-1]


word1 = "horse"
word2 = "ros"
        
test = Solution()
print test.minDistance(word1,word2)