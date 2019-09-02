# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:36:15 2019

@author: Tianqi Guo
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """        
        l = len(citations)   
        h, t = 0, l - 1        
        while h <= t:            
            m = (h + t)/2
            if citations[m] >= l - m:
                t = m - 1
            else:
                h = m + 1
        return l - h

citations = [0,1,3,5,6]
citations = [1,2]
citations = [0, 1]
citations = [11,15]

citations = [100]

test = Solution()
print(test.hIndex(citations))