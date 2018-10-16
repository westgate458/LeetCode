# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:05:27 2018

@author: Tianqi Guo
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = ['CM','CD','XC','XL','IX','IV',
             'M','D','C','L','X','V','I']
        n = [900,400,90,40,9,4,
             1000,500,100,50,10,5,1]          
        num = 0
        p = 0
        roman = ' ' + s + ' '
        while roman != '  ':
            pos = roman.find(r[p])            
            if pos != -1:
                num = num + n[p]                
                roman = roman[0:pos]+roman[pos+len(r[p]):]
            else:
                p = p + 1
        return(num)
s = 'MCMXCIV'
test = Solution()
print(test.romanToInt(s))                
            