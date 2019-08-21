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
        
        # dictionary to memorize already-solved problems
        self.d = {}
        
        # function solving sub problems (diffWaysToCompute(s[p:pp+1])) recursively
        def helper(s, p, pp):     
            # if current sub problem has already been solved before
            if (p,pp) in self.d:
                # load it from memory and return
                return self.d[(p, pp)]          
            # if current segment is only a number with no operations
            elif s[p:pp+1].isdigit():
                # save the value into memory
                self.d[(p, pp)] = [int(s[p:pp+1])]                
            # if current segment is a sub problem that needs to be solved
            else:     
                # initialize solution for current sub problem
                self.d[(p, pp)] = []         
                # check each character in the string segment
                for i in range(p,pp+1):               
                    # if we have found an operator, split the segment into left and right
                    if s[i] in '+-*':        
                        # solve the left and right sub problems
                        # and for all possible combinations from the left and right sets of results
                        for l in helper(s,p,i-1):
                            for r in helper(s,i+1,pp):
                                # depending on the current operator, perform the calculation
                                # and update the result set for current segment
                                if s[i] == '+':
                                    self.d[(p, pp)] += [l + r]
                                elif s[i] == '-':
                                    self.d[(p, pp)] += [l - r]
                                else:
                                    self.d[(p, pp)] += [l * r]
            # return the solution for current segment                        
            return self.d[(p, pp)]             
        # solve the original problem top-down
        return helper(input, 0, len(input)-1)

s = "2-1-1"    
s = "2*3-4*5"
test = Solution()
print(test.diffWaysToCompute(s))
                                
                        
                        
            
            
            
            
            
            
            
            
            
            
            
            
            