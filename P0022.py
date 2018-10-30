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
        combo = [['()']]
        for i in range(1,n):
            new_combo = []
            lst_combo = combo[i-1]
            for j in range(len(lst_combo)):
                new_combo.append('('+lst_combo[j]+')')            
            for j in range(i):
                combo_1 = combo[j]
                combo_2 = combo[i-j-1]
                for ii in range(len(combo_1)):
                    for jj in range(len(combo_2)):
                        if not (combo_1[ii]+combo_2[jj] in new_combo):
                            new_combo.append(combo_1[ii]+combo_2[jj])                        
            combo.append(new_combo)            
        return combo[n-1]

n = 3
test = Solution()
print(test.generateParenthesis(n))
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    