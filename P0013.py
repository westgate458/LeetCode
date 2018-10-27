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
        # all the Roman character combos
        # CM, CD, XC, XL, IX, IV follow the subtraction rule
        # and are treated before the summation rules
        r = ['CM','CD','XC','XL','IX','IV',
             'M','D','C','L','X','V','I']
        # decimal numbers correspond to each Roman character combo
        n = [900,400,90,40,9,4,
             1000,500,100,50,10,5,1]    
        # set initial decimal number and the pointer for r-list to 0's
        num = 0
        p = 0
        # blankspace-padding the Roman number to avoid out of bound error
        roman = ' ' + s + ' '
        # repeat conversion until all Roman characters are summed up
        while roman != '  ':
            # try to find the p-th Roman character combo from r-list
            # in the remaining Roman string
            pos = roman.find(r[p])  
            # if the p-th Roman character combo exists in the string
            if pos != -1:
                # add the corresponding value to result                
                num = num + n[p]                
                # remove the already found-and-summed substring
                roman = roman[0:pos]+roman[pos+len(r[p]):]
            else:
                # if the p-th Roman character combo doesn't exist
                # update p pointer to the next Roman character combo
                p = p + 1
        return(num)
        
s = 'MCMXCIV'
test = Solution()
print(test.romanToInt(s))                
            