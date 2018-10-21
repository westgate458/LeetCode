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
        
        c = [['a','b','c'],
             ['d','e','f'],
             ['g','h','i'],
             ['j','k','l'],
             ['m','n','o'],
             ['p','q','r','s'],
             ['t','u','v'],
             ['w','x','y','z']]
        
        l = len(digits)
        if l == 0:
            return []
        s = [""]
        for i in range(l):
            num = int(digits[i])
            ss = []
            while s:
                sss = s.pop(0)                
                for j in range(len(c[num-2])):
                    ss.append(sss+c[num-2][j])
            s = ss        
        return s    
digits = ""
test = Solution()
print(test.letterCombinations(digits))             
            
            
            
            
            
            
            
            
            
            