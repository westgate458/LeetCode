# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:00:08 2019

@author: Tianqi Guo
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0:
            return 'Zero'
        
        ones = ['','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['','Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens = ['','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen','Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        units = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
        
        words = ''
        
        counter = -1
        while num:
            
            counter += 1            
            c = num % 1000
            num //= 1000
            
            seg = ''
            
            hs = c // 100
            ts = c //10 - hs * 10
            os = c % 10
            
            if hs > 0:
                seg += ' ' + ones[hs] + ' Hundred'
            
            if ts == 1:
                if os == 0:
                    seg += ' Ten'
                else:
                    seg += ' ' + teens[os]
            elif ts > 0:               
                seg += ' ' + tens[ts]
            
            if ts != 1 and os > 0:
                seg += ' ' + ones[os]
                
            if seg != '':
                words = seg + ' ' + units[counter] + words     

        return words.strip()



num = 12345
test = Solution()
print(test.numberToWords(num))