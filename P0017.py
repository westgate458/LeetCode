# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:05:51 2018

@author: Tianqi Guo
"""

class Solution(object):
   
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # the characters corresponding to each number
        c = [['a','b','c'],
             ['d','e','f'],
             ['g','h','i'],
             ['j','k','l'],
             ['m','n','o'],
             ['p','q','r','s'],
             ['t','u','v'],
             ['w','x','y','z']]        
        # deal with the situation of an empty list
        l = len(digits)
        if l == 0:
            return []
        # the queue that stores all combinations by previous digits
        s = [""]
        # iterate over all digits
        for i in range(l):
            # get the current digit
            num = int(digits[i])
            # the queue that stores all new combinations
            ss = []
            # iterate over all previous combinations
            while s:
                # for each previous combination                
                sss = s.pop(0)
                # combine with the characters for current digit
                for j in range(len(c[num-2])):
                    # record all new combinations
                    ss.append(sss+c[num-2][j])
            # copy the new combinations to the queue
            s = ss        
        return s    
    
digits = "23"
test = Solution()
print(test.letterCombinations(digits))             
            
            
            
            
            
            
            
            
            
            