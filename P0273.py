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
        
        # deal with trivial case
        if num == 0:
            return 'Zero'
        
        # the english words for each digit
        ones = ['','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['','Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens = ['','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen','Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        units = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
        
        # start with empty string
        words = ''
        
        # count how many 'three digits' we have seen
        counter = -1
        # continue iteration until all digits are dealt with
        while num:
            # update counter
            counter += 1    
            # take the next three digits
            # update number
            c = num % 1000
            num //= 1000
            # word for current unit
            seg = ''
            # take the individual digits: hundreds, tens, and ones
            hs = c // 100
            ts = c //10 - hs * 10
            os = c % 10
            # deal with the hundreds
            if hs > 0:
                seg += ' ' + ones[hs] + ' Hundred'
            # deal with special case of 10 ~ 19
            if ts == 1:
                if os == 0:
                    seg += ' Ten'
                else:
                    seg += ' ' + teens[os]
            # deal with other tens: 20 ~ 90
            elif ts > 0:               
                seg += ' ' + tens[ts]
            # deal with the ones, especially check if it is 10 ~ 19
            if ts != 1 and os > 0:
                seg += ' ' + ones[os]
            # if current unit is not '000', add the unit and update words
            if seg != '':
                words = seg + ' ' + units[counter] + words     
        
        # return the converted words with leading and trailing spaces removed
        return words.strip()



num = 12345
test = Solution()
print(test.numberToWords(num))