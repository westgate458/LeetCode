# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:41:45 2018

@author: Tianqi Guo
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # characters in each row after conversion
        zigzag = [[] for i in range(numRows)]
        # current row number
        row_num = -1
        # direction of zigzag, 0 downwards, 1 upwards
        direction = 0
        # for all characters in s, one by one
        for i in range(len(s)):
            # if proceed downwards
            if direction == 0:
                # if not arrived at the last row
                if row_num < numRows - 1:
                    # update the row number
                    row_num = row_num + 1            
                else:
                    # if has arrived at the last row
                    # change direction and update the row number
                    direction = 1
                    row_num = row_num - 1
            else:
                # if proceed upwards
                # if not arrived at the first row
                if row_num > 0:
                    # update the row number
                    row_num = row_num - 1            
                else:
                    # if has arrived at the first row
                    # change direction and update the row number
                    direction = 0
                    row_num = row_num + 1 
            # append current character to the row list
            zigzag[row_num].append(s[i])
        # convert the zigzag list to the answer format
        ans = ''
        for i in range(numRows):
            for j in range(len(zigzag[i])):
                # add each character to the answer string
                # row by row, character by character
                ans = ans + zigzag[i][j]
        
        # return answer
        return ans
    
s = "PAYPALISHIRING"
numRows = 4            
test = Solution()
print(test.convert(s, numRows))
     
   
            
            
            
            
        

    
    