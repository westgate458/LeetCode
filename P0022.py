# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:13:12 2018

@author: Tianqi Guo
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """       
        # initial answer list with n == 1
        # index i of combo corresponds to n = i + 1
        combo = [['()']]
        
        # for each n get combinations from previous n's
        for i in range(1,n):
            
            # combination list for current n
            new_combo = []
            # combination list from previous n
            lst_combo = combo[i-1]
            
            # Part 1 of combinations for current n == i + 1            
            for j in range(len(lst_combo)):
                # ( + previous combinations + )
                new_combo.append('('+lst_combo[j]+')')            
            
            # Part 2 of combinations for current n == i + 1
            for j in range(i):
                # sets of (combo from n == j) and (combo from n == i - j - 1)
                combo_1 = combo[j]
                combo_2 = combo[i-j-1]
                # all combinations formed by elements from the two sets
                for ii in range(len(combo_1)):
                    for jj in range(len(combo_2)):
                        # add to answer list if it doesn't already exist
                        if not (combo_1[ii]+combo_2[jj] in new_combo):
                            new_combo.append(combo_1[ii]+combo_2[jj])   
            
            # add the combo for current n to the answer list
            combo.append(new_combo)            
            
        # return combinations for n = n - 1 + 1
        return combo[n-1]

n = 3
test = Solution()
print(test.generateParenthesis(n))
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    