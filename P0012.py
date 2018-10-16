# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:37:03 2018

@author: Tianqi Guo
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """              
        r4 = ['','M','MM','MMM']
        r3 = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        r2 = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        r1 = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        d4 = num/1000
        d3 = num/100 - d4 * 10
        d2 = num/10 - d3 * 10 - d4 * 100
        d1 = num%10        
        return(r4[d4] + r3[d3] + r2[d2] + r1[d1])        
        
num = 1994
test = Solution()
print(test.intToRoman(num))