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
        
        # lenghs of two words
        l1 = len(word1)
        l2 = len(word2)
        
        # initialize state functions
        # pad with boundary values (0)
        steps = [range(l2+1)] + [[x]+[0]* l2 for x in range(1,l1+1)]
        
        # determine states (steps) from previous states
        for m in range(1,l1+1):
            for n in range(1,l2+1):  
                # if the ending characters match
                if word1[m-1] == word2[n-1]:
                    # no need to edit, save steps as the previous state
                    steps[m][n] = steps[m-1][n-1]
                # if the ending characters do not match
                else:
                    # current steps is the minimum of the three:
                    # 1) delete one character from Word 1
                    # 2) add one character to Word 1
                    # 3) replace one character
                    # plus corresponding previous states
                    steps[m][n] = min(steps[m-1][n],steps[m][n-1],steps[m-1][n-1]) + 1
        
        # return the final state (steps)
        return steps[-1][-1]


word1 = "horse"
word2 = "ros"
        
test = Solution()
print test.minDistance(word1,word2)