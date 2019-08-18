# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:20:03 2019

@author: Tianqi Guo
"""

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        self.d = {}
        
        def helper(s, p, pp):               
            if (p,pp) in self.d:
                return self.d[(p, pp)]            
            elif s[p:pp+1].isdigit():
                self.d[(p, pp)] = [int(s[p:pp+1])]                
            else:     
                self.d[(p, pp)] = []                
                for i in range(p,pp+1):                    
                    if s[i] in '+-*':                        
                        for l in helper(s,p,i-1):
                            for r in helper(s,i+1,pp):
                                if s[i] == '+':
                                    self.d[(p, pp)] += [l + r]
                                elif s[i] == '-':
                                    self.d[(p, pp)] += [l - r]
                                else:
                                    self.d[(p, pp)] += [l * r]
                                    
            return self.d[(p, pp)]             
        
        return helper(input, 0, len(input)-1)

s = "2-1-1"    
s = "2*3-4*5"
test = Solution()
print(test.diffWaysToCompute(s))
                                
                        
                        
            
            
            
            
            
            
            
            
            
            
            
            
            