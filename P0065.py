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
        
        # legit numbers
        nums = '0123456789'
        
        # sub function checking if string is a number
        def check(s): 
            # legal string can only contain one '.'
            # and only one '+' at the beginning
            # the rest should only be numbers  
            
            # remove leading '+' if exists
            if s.find('+') == 0:
                s = s[1:]  
            
            # remove first '.' if exists
            d_pos = s.find('.')
            if d_pos != -1:
                s = s[:d_pos] + s[d_pos+1:]
            
            # if string is empty after removing '.' and '+'           
            if s == '':
                # it is not legal, return false
                return False            
            
            # check if each remaining character is a number
            for c in s:
                # if illegal character is found
                if nums.find(c) == -1:
                    # return false
                    return False 
            
            # if string passes all tests, it is legal  
            return True
        
        # removing leading and trailing white spaces 
        s = s.strip()
        # replace '-'s with equivalent '+'s
        s = s.replace('-','+')
        # find position of 'e' if exists
        e_pos = s.find('e')
        # if 'e' doesn't exists
        if e_pos == -1:
            # check original s directly
            return check(s)     
        # if 'e' exists
        else:
            # split the string into two halves
            s_l = s[:e_pos]
            s_r = s[e_pos+1:]
            # check if the right string has '.'
            d_pos = s_r.find('.')
            # if it has '.', string is illegal for some reason
            if d_pos!= -1:
                return False
            # check two halves separately
            return check(s_l) and check(s_r)
        
        # if string passes all tests, it is legal  
        return True

s_set = ['0','.-4']           
test = Solution()
for s in s_set:
    print s
    print test.isNumber(s)
    print ''
            
    
