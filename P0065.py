# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:39:28 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        nums = '0123456789'
        
        def check(s): 
            s_pos = s.find('+')
            if s_pos == 0:
                s = s[:s_pos] + s[s_pos+1:]  
                
            d_pos = s.find('.')
            if d_pos != -1:
                s = s[:d_pos] + s[d_pos+1:]
                
            if s == '':
                return False            
            
            for c in s:
                if nums.find(c) == -1:
                    return False 
                
            return True
            
        s = s.strip()
        if len(s) == 0:
            return False        
        
        s = s.replace('-','+')
        
        e_pos = s.find('e')
        if e_pos == -1:
            return check(s)          
        else:
            
            s_l = s[:e_pos]
            s_r = s[e_pos+1:]
            
            d_pos = s_r.find('.')
            if d_pos!= -1:
                return False
            
            return check(s_l) and check(s_r)
        
        return True

s_set = ['0','.-4']           
test = Solution()
for s in s_set:
    print s
    print test.isNumber(s)
    print ''
            
    
